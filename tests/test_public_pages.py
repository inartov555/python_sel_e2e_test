from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest

"""
Tests for an unauthorized user
"""

import pytest

from tools.logger.logger import Logger

log = Logger(__name__)


@pytest.mark.usefixtures('setup_elements_for_test')
class TestPublicPages:
    """
    Tests for an unauthorized user
    """

    def test_landing_links_present(self):
        """
        Open the landing driver -> check if the driver is loaded
        """
        self.landing_page.open()
        self.login_page.allow_all_cookies_if_shown()
        self.landing_page.expect_loaded()

    def test_navigate_to_login(self):
        """
        Open the landing driver -> select the sign up element -> select the login element
        """
        self.landing_page.open()
        self.login_page.allow_all_cookies_if_shown()
        self.landing_page.go_to_signup()
        self.signup_page.go_to_login()
        self.login_page.expect_loaded()

    def test_navigate_to_signup(self):
        """
        Open the landing driver -> select the sign up element -> check the driver is loaded
        """
        self.landing_page.open()
        self.login_page.allow_all_cookies_if_shown()
        self.landing_page.go_to_signup()
        self.signup_page.expect_loaded()

    def test_login_negative_incorrect_creds(self):
        """
        Open the login driver -> check if the driver is loaded -> enter the incorrect credentials -> check the error text
        """
        self.login_page.open()
        self.login_page.allow_all_cookies_if_shown()
        self.login_page.expect_loaded()
        self.login_page.login("incorrect_user@example.com", "wrong_password")
        self.login_page.expect_error_login()