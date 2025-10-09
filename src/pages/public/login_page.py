"""
Login page
"""

from __future__ import annotations

from selenium.webdriver.common.by import By

from src.core.ui import Ui
from src.core.app_config import AppConfig
from src.pages.base_page import BasePage
from src.pages.components.login_form import LoginForm
from src.pages.components.cookie_banner import CookieBanner
from tools.logger.logger import Logger


log = Logger(__name__)


class LoginPage(BasePage):
    """
    Login page
    """
    def __init__(self, app_config: AppConfig, ui_driver: Ui):
        """
        /accounts/login/ - URI path

        Args:
            app_config (AppConfig): app config passed in ini config file
            ui_driver (Ui): selenenium web driver adapter
        """
        super().__init__(app_config, "/accounts/login/", ui_driver)
        self.login_form = LoginForm
        self.forgot_password = (By.CSS_SELECTOR, 'a[href="/accounts/password/reset/"]')

    def allow_all_cookies_if_shown(self) -> bool:
        """
        Confirming the allow cookies overlay, if shown
        """
        return CookieBanner(self.ui_driver).accept_if_present()

    def form(self) -> LoginForm:
        """
        Get login form
        """
        return self.login_form(self.ui_driver)

    def login(self, username: str, password: str) -> None:
        """
        Log in
        """
        self.form().expect_loaded()
        self.form().login(username, password)

    def expect_error_login(self) -> None:
        """
        Verifying if error test is shown when login failed due to incorrect credentials
        """
        self.form().expect_loaded()
        self.form().expect_error_login()

    def expect_loaded(self) -> None:
        """
        Verifying if the Log in page's landing image is shown
        """
        self.ui_driver.wait_for_dom_ready()
        self.form().expect_loaded()
