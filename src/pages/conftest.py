"""
conftest.py
"""

import pytest

from src.core.ui import Ui
from src.pages.public.landing_page import LandingPage
from src.pages.public.login_page import LoginPage
from src.pages.public.signup_page import SignupPage
from src.pages.private.home_feed_page import HomeFeedPage
from tools.logger.logger import Logger


log = Logger(__name__)


@pytest.fixture(autouse=False, scope="function")
def setup_elements_for_test(request) -> None:
    """
    Setting up the object for a test
    """
    app_config = request.getfixturevalue("app_config")
    driver = request.node.stash["webdriver_obj_fresh"]
    request.cls.app_config = app_config
    ui_driver = Ui(driver)
    request.cls.landing_page = LandingPage(app_config, ui_driver)
    request.cls.signup_page = SignupPage(app_config, ui_driver)
    request.cls.login_page = LoginPage(app_config, ui_driver)
    request.cls.home_page = HomeFeedPage(app_config, ui_driver)
