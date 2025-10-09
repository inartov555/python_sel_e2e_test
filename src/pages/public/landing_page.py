from __future__ import annotations

from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from src.pages.components.cookie_banner import CookieBanner

class LandingPage(BasePage):
    @property
    def path(self) -> str:
        return "/"

    LOGIN_LINK = (By.CSS_SELECTOR, 'a[href="/accounts/login/?source=auth_switcher"]')
    SIGNUP_LINK = (By.CSS_SELECTOR, 'a[href="/accounts/emailsignup/"]')
    HERO_IMG = (By.CSS_SELECTOR, 'img[src*="/images/"]')

    def accept_cookies_if_shown(self) -> bool:
        return CookieBanner(self.driver).accept_if_present()

    def expect_loaded(self) -> None:
        self.ui.wait_for_dom_ready()
        self.ui.wait_visible(self.LOGIN_LINK)
        self.ui.wait_visible(self.SIGNUP_LINK)
