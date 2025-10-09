import os
from typing import Generator

import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from src.core.driver import build_driver
from src.pages.public.landing_page import LandingPage
from src.pages.public.login_page import LoginPage
from src.pages.public.signup_page import SignupPage
from src.pages.private.home_feed_page import HomeFeedPage

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="chrome|chromium|msedge|firefox|safari")
    parser.addoption("--headed", action="store_true", default=False,
                     help="Show browser UI (disable headless)")
    parser.addoption("--username", action="store", default=None, help="Instagram username")
    parser.addoption("--password", action="store", default=None, help="Instagram password")

@pytest.fixture(scope="session")
def driver(request) -> Generator[WebDriver, None, None]:
    browser = request.config.getoption("--browser")
    headed = request.config.getoption("--headed")
    drv = build_driver(browser=browser, headless=(not headed), window_size=(1920, 1080))
    yield drv
    drv.quit()

@pytest.fixture
def landing_page(driver) -> LandingPage:
    return LandingPage(driver)

@pytest.fixture
def login_page(driver) -> LoginPage:
    return LoginPage(driver)

@pytest.fixture
def signup_page(driver) -> SignupPage:
    return SignupPage(driver)

@pytest.fixture
def home_feed_page(driver, request) -> HomeFeedPage:
    return HomeFeedPage(driver)

@pytest.fixture
def creds(request):
    return {
        "username": request.config.getoption("--username") or os.getenv("IG_USERNAME"),
        "password": request.config.getoption("--password") or os.getenv("IG_PASSWORD"),
    }
