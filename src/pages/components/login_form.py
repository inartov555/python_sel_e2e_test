"""
Login form
"""

from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from tools.logger.logger import Logger
from src.core.ui import Ui
from src.pages.components.base_component import BaseComponent


log = Logger(__name__)


class LoginForm(BaseComponent):
    """
    Login form
    """
    def __init__(self, ui_driver: Ui, web_elem: WebElement = None):
        """
        Args:
            ui_driver (Ui): selenenium web driver adapter
            web_elem (WebElement): web element
        """
        super().__init__(ui_driver, web_elem)
        self.root = (By.CSS_SELECTOR, "form#loginForm")
        self.username = (By.CSS_SELECTOR, 'input[name="username"]')
        self.password = (By.CSS_SELECTOR, 'input[name="password"]')
        self.submit = (By.CSS_SELECTOR, 'button[type="submit"]')
        self.error_area = (
            By.XPATH,
            '//*[@role="alert"] | //*[@id="slfErrorAlert"] | //div[contains(normalize-space(.), "incorrect")]'
        )
        self.incorrect_login_error_text = (
            By.XPATH,
            '//*[normalize-space(.)="Sorry, your password was incorrect. Please double-check your password."]'
        )

    def expect_loaded(self) -> None:
        """
        Checking if there are some elemeing in the login form
        """
        self.ui_driver.wait_visible(self.root)
        self.ui_driver.wait_visible(self.username)
        self.ui_driver.wait_visible(self.password)

    def login(self, username: str, password: str) -> None:
        """
        Logging in
        """
        self.ui_driver.clear(self.username)
        self.ui_driver.send_keys(username, self.username)
        self.ui_driver.clear(self.password)
        self.ui_driver.send_keys(password, self.password)
        self.ui_driver.click(self.submit)

    def expect_error_login(self) -> None:
        """
        Verifying if error test is shown when login failed due to incorrect credentials
        """
        log.info("Verifying if error log in text is shown")
        if not self.ui_driver.wait_visible(self.incorrect_login_error_text):
            raise AssertionError(f"{self.incorrect_login_error_text element} is not visible")
