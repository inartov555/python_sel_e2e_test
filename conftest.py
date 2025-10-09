"""
conftest.py file
"""

import os
from typing import Generator
from configparser import ConfigParser, ExtendedInterpolation

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.remote.webdriver import WebDriver

from src.core.app_config import AppConfig
from tools.file_utils import FileUtils
from tools.logger.logger import Logger
from tools.temp_encr import decrypt


log = Logger(__name__)


# Register fixture modules so tests can use them without importing symbols
pytest_plugins = [
    "src.pages.conftest",
    "src.pages.private.conftest",
]


@pytest.fixture(autouse=True, scope="session")
def add_loggers():
    """
    The fixture to configure loggers
    It uses built-in pytest arguments to configure loggigng level and files

    Parameters:
        log_level or --log-level general log level for capturing
        log_file_level or --log-file-level  level of log to be stored to a file. Usually lower than general log
        log_file or --log-file  path where logs will be saved
    """
    artifacts_folder_default = os.getenv("HOST_ARTIFACTS")
    log_level = "DEBUG"
    log_file_level = "DEBUG"
    log_file = os.path.join(FileUtils.timestamped_path("pytest", "log", artifacts_folder_default))
    log.setup_cli_handler(level=log_level)
    log.setup_filehandler(level=log_file_level, file_name=log_file)
    log.info(f"General loglevel: '{log_level}', File: '{log_file_level}'")
    log.info(f"Test logs will be stored: '{log_file}'")


def validate_app_config_params(**kwargs) -> None:
    """
    Validation of the config parameters
    """
    if not kwargs.get("username"):
        raise ValueError("username parameter is required for tests")
    if not kwargs.get("password"):
        raise ValueError("password parameter is required for tests")


@pytest.fixture(scope="session")
def app_config(pytestconfig) -> AppConfig:
    """
    Set and get AppConfig from ini config
    """
    ini_config_file = pytestconfig.getoption("--ini-config")
    log.info(f"Reading config properties from '{ini_config_file}' and storing to a data class")
    result_dict = {}
    cfg = ConfigParser(interpolation=ExtendedInterpolation())
    cfg.read(ini_config_file)
    result_dict["wait_to_handle_capture_manually"] = cfg.getboolean("pytest",
                                                                    "wait_to_handle_capture_manually",
                                                                    fallback=False)
    result_dict["action_timeout"] = cfg.getfloat("pytest", "action_timeout", fallback=15000.0)
    result_dict["navigation_timeout"] = cfg.getfloat("pytest", "navigation_timeout", fallback=15000.0)
    result_dict["assert_timeout"] = cfg.getfloat("pytest", "assert_timeout", fallback=15000.0)
    result_dict["browser"] = cfg.get("pytest", "browser", fallback="chrome")
    result_dict["base_url"] = cfg.get("pytest", "base_url", fallback="https://www.instagram.com")
    result_dict["is_headless"] = cfg.getboolean("pytest", "is_headless", fallback=False)
    result_dict["width"] = cfg.getint("pytest", "width", fallback=1920)
    result_dict["height"] = cfg.getint("pytest", "height", fallback=1080)
    result_dict["username"] = cfg.get("pytest", "username")
    result_dict["password"] = cfg.get("pytest", "password")
    validate_app_config_params(**result_dict)
    result_dict["password"] = decrypt(result_dict.get("password"))
    return AppConfig(**result_dict)


def pytest_addoption(parser):
    """
    Supported options
    """
    parser.addoption("--ini-config", action="store", default="pytest.ini", help="The path to the *.ini config file")


@pytest.fixture(scope="session")
def screenshot_dir() -> str:
    """
    Getting screenshot directory
    """
    artifacts_folder_default = os.getenv("HOST_ARTIFACTS")
    os.makedirs(artifacts_folder_default, exist_ok=True)
    return artifacts_folder_default


def get_browser(request) -> WebDriver:
    """
    Set up a Selenium WebDriver and return it.
    Uses Selenium Manager (Selenium >= 4.6), so no webdriver-manager needed.
    """
    log.info("Getting a browser basing on the config properties")
    _app_config = request.getfixturevalue("app_config")
    browser = _app_config.browser.lower()
    width, height = int(_app_config.width), int(_app_config.height)
    headless = bool(_app_config.is_headless)

    # Convert ms (Playwright-style) -> seconds (Selenium)
    nav_s    = float(_app_config.navigation_timeout) / 1000.0
    action_s = float(_app_config.action_timeout)     / 1000.0
    assert_s = float(_app_config.assert_timeout)     / 1000.0
    if browser in ("chrome", "chromium"):
        opts = ChromeOptions()
        if headless:
            opts.add_argument("--headless=new")
        opts.add_argument(f"--window-size={width},{height}")
        opts.add_argument("--no-sandbox")
        opts.add_argument("--disable-dev-shm-usage")

        # If you truly want Chromium instead of Chrome, optionally point to the binary:
        if browser == "chromium" and getattr(_app_config, "chromium_binary", None):
            opts.binary_location = _app_config.chromium_binary
        driver = webdriver.Chrome(options=opts)
    elif browser == "msedge":
        opts = EdgeOptions()
        if headless:
            opts.add_argument("--headless=new")
        opts.add_argument(f"--window-size={width},{height}")
        driver = webdriver.Edge(options=opts)
    elif browser == "firefox":
        opts = FirefoxOptions()
        if headless:
            opts.add_argument("-headless")   # Firefox uses single dash
        driver = webdriver.Firefox(options=opts)
        # Firefox respects size best after startup:
        driver.set_window_size(width, height)
    elif browser in ("safari", "webkit"):
        # macOS only; no headless
        if headless:
            log.warning("Headless is not supported for Safari/WebKit; starting headed.")
        opts = SafariOptions()
        driver = webdriver.Safari(options=opts)
        driver.set_window_size(width, height)
    else:
        raise ValueError(f"browser config param contains incorrect value: {browser}")
    # Map Playwright timeouts to Selenium equivalents
    driver.set_page_load_timeout(nav_s)   # navigation timeout
    driver.set_script_timeout(action_s)   # async script timeout
    # (No global 'assert' timeout in Selenium; keep it for your waits)
    request.node.stash["assert_timeout_secs"] = assert_s

    # Stash raw driver for other fixtures/POs (mirrors your Playwright stash)
    request.node.stash["webdriver_obj_fresh"] = driver

    log.info(f"{browser} browser is selected")
    return driver


@pytest.fixture(autouse=True, scope="function")
def browser_setup(request):
    """
    Set the browser driver
    """
    browser = get_browser(request)
    yield browser
    browser.close()
