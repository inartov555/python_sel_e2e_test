from __future__ import annotations

from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from src.pages.components.cookie_banner import CookieBanner

class SignupPage(BasePage):
    @property
    def path(self) -> str:
        return "/accounts/emailsignup/"

    EMAIL_OR_PHONE = (By.CSS_SELECTOR, 'input[name="emailOrPhone"]')
    FULL_NAME = (By.CSS_SELECTOR, 'input[name="fullName"]')
    USERNAME = (By.CSS_SELECTOR, 'input[name="username"]')
    PASSWORD = (By.CSS_SELECTOR, 'input[name="password"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[type="submit"]')
    LOGIN_LINK = (By.CSS_SELECTOR, 'a[href="/accounts/login/?source=auth_switcher"]')

    def accept_cookies_if_shown(self) -> bool:
        return CookieBanner(self.driver).accept_if_present()

    def expect_loaded(self) -> None:
        self.ui.wait_for_dom_ready()
        self.ui.wait_visible(self.EMAIL_OR_PHONE)
        self.ui.wait_visible(self.USERNAME)
        self.ui.wait_visible(self.PASSWORD)
        self.ui.wait_visible(self.LOGIN_LINK)
