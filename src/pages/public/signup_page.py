"""
Signup page
"""

from __future__ import annotations

from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage
from src.pages.components.cookie_banner import CookieBanner
from tools.logger.logger import Logger


log = Logger(__name__)


class SignupPage(BasePage):
    """
    Signup page
    """
    def __init__(self, app_config: AppConfig, ui_driver: Ui):
        """
        /accounts/emailsignup/ - URI path

        Args:
            app_config (AppConfig): app config passed in ini config file
            ui_driver (Ui): selenenium web driver adapter
        """
        super().__init__(app_config, "/accounts/emailsignup/", ui_driver)
        self.EMAIL_OR_PHONE = (By.CSS_SELECTOR, 'input[name="emailOrPhone"]')
        self.FULL_NAME = (By.CSS_SELECTOR, 'input[name="fullName"]')
        self.USERNAME = (By.CSS_SELECTOR, 'input[name="username"]')
        self.PASSWORD = (By.CSS_SELECTOR, 'input[name="password"]')
        self.SUBMIT = (By.CSS_SELECTOR, 'button[type="submit"]')
        self.LOGIN_LINK = (By.CSS_SELECTOR, 'a[href="/accounts/login/?source=auth_switcher"]')

    def accept_cookies_if_shown(self) -> bool:
        """
        Accpet cookies overlay, if shown
        """
        return CookieBanner(self.ui_driver).accept_if_present()

    def expect_loaded(self) -> None:
        """
        Checking if page has some elements
        """
        self.ui_driver.wait_for_dom_ready()
        self.ui_driver.wait_visible(self.EMAIL_OR_PHONE)
        self.ui_driver.wait_visible(self.USERNAME)
        self.ui_driver.wait_visible(self.PASSWORD)
        self.ui_driver.wait_visible(self.LOGIN_LINK)

    def go_to_login(self) -> None:
        """
        Go to login
        """
        log.info("Go to log in")
        self.ui_driver.wait_clickable(self.LOGIN_LINK)
        self.ui_driver.click(self.LOGIN_LINK)
