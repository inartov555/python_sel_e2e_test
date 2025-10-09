from __future__ import annotations

from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from src.pages.components.login_form import LoginForm
from src.pages.components.cookie_banner import CookieBanner

class LoginPage(BasePage):
    @property
    def path(self) -> str:
        return "/accounts/login/"

    FORM = LoginForm
    FORGOT_PASSWORD = (By.CSS_SELECTOR, 'a[href="/accounts/password/reset/"]')

    def allow_all_cookies_if_shown(self) -> bool:
        return CookieBanner(self.driver).accept_if_present()

    def expect_loaded(self) -> None:
        self.ui.wait_for_dom_ready()
        self.ui.wait_visible((By.CSS_SELECTOR, "form#loginForm"))
        self.ui.wait_visible(self.FORGOT_PASSWORD)

    def form(self) -> LoginForm:
        return self.FORM(self.driver)
