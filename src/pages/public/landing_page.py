from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest

"""
Landing driver
"""

from __future__ import annotations


from tools.logger.logger import Logger
from src.core.app_config import AppConfig
from src.core.ui_driver import UIDriver
from src.pages.base_page import BasePage
from src.components.login_form import LoginForm


log = Logger(__name__)


class LandingPage(BasePage):
    """
    Landing driver
    """
    def __init__(self, app_config: AppConfig, ui_driver: UIDriver):
        """
        / - URI path

        Args:
            app_config (AppConfig): app config passed in ini config file
            ui_driver (UIDriver): e.g., PlaywrightDriver adapter
        """
        super().__init__(app_config, "/", ui_driver)
        self.login_form_root = self.locator('form[id="loginForm"]')
        self.signup_link = self.locator('a[href="/accounts/emailsignup/"]')
        self.landing_image = self.locator('img[src="/images/assets_DO_NOT_HARDCODE/lox_brand/landing-2x.png"]')

    def login(self, username: str, password: str) -> None:
        """
        Log in
        """
        expect(self.login_form_root).to_be_visible()
        login_form = LoginForm(self.login_form_root, self)
        login_form.login(username, password)

    def expect_error_login(self) -> None:
        """
        Verifying if error test is shown when login failed due to incorrect credentials
        """
        expect(self.login_form_root).to_be_visible()
        login_form = LoginForm(self.login_form_root, self)
        login_form.expect_error_login()

    def go_to_signup(self) -> None:
        """
        Go to the Sign up driver
        """
        log.info("Go to the Sign up driver")
        self.signup_link.click()

    def expect_loaded(self) -> None:
        """
        Verifying if the Log in driver's landing image is shown
        """
        log.info("Verifying if the Log in driver's landing image is shown")
        expect(self.landing_image).to_be_visible()