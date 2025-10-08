from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


"""
conftest.py
"""

import pytest

from src.pages.public.landing_page import LandingPage
from src.pages.public.login_page import LoginPage
from src.pages.public.signup_page import SignupPage
from src.pages.private.home_feed_page import HomeFeedPage
from src.core.playwright_driver import PlaywrightDriver
from tools.logger.logger import Logger

log = Logger(__name__)

@pytest.fixture(autouse=False, scope="function")
def setup_elements_for_test(request, driver) -> None:
    """
    Setting up the object for a test
    """
    app_config = request.getfixturevalue("app_config")
    page_obj = request.node.stash.get("page_obj_fresh", driver)
    request.cls.app_config = app_config
    playwright_driver = PlaywrightDriver(app_config, page_obj)
    request.cls.landing_page = LandingPage(app_config, playwright_driver)
    request.cls.signup_page = SignupPage(app_config, playwright_driver)
    request.cls.login_page = LoginPage(app_config, playwright_driver)
    request.cls.home_page = HomeFeedPage(app_config, playwright_driver)