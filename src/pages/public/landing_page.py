"""
Landing page
"""

from __future__ import annotations

from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage
from src.pages.components.cookie_banner import CookieBanner
from src.pages.components.login_form import LoginForm
from tools.logger.logger import Logger


log = Logger(__name__)


class LandingPage(BasePage):
    """
    Landing page
    """
    def __init__(self, app_config: AppConfig, ui_driver: Ui):
        """
        / - URI path

        Args:
            app_config (AppConfig): app config passed in ini config file
            ui_driver (Ui): selenenium web driver adapter
        """
        super().__init__(app_config, "/", ui_driver)
        self.FORM = LoginForm
        self.LOGIN_LINK = (By.CSS_SELECTOR, 'a[href="/accounts/login/?source=auth_switcher"]')
        self.SIGNUP_LINK = (By.CSS_SELECTOR, 'a[href="/accounts/emailsignup/"]')
        self.HERO_IMG = (By.CSS_SELECTOR, 'img[src*="/images/"]')
        self.LANDING_IMAGE = (By.CSS_SELECTOR, 'img[src="/images/assets_DO_NOT_HARDCODE/lox_brand/landing-2x.png"]')

    def form(self) -> LoginForm:
        return self.FORM(self.ui_driver)

    def accept_cookies_if_shown(self) -> bool:
        return CookieBanner(self.ui_driver).accept_if_present()

    def expect_loaded(self) -> None:
        """
        Verifying if the Log in page's landing image is shown
        """
        log.info("Verifying if the Log in page's landing image is shown")
        self.ui_driver.wait_visible(self.LANDING_IMAGE)

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

    def go_to_signup(self) -> None:
        """
        Go to the Sign up page
        """
        log.info("Go to the Sign up page")
        self.ui_driver.wait_visible(self.SIGNUP_LINK)
        self.ui_driver.click(self.SIGNUP_LINK)
