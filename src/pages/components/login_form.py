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
        self.ROOT = (By.CSS_SELECTOR, "form#loginForm")
        self.USERNAME = (By.CSS_SELECTOR, 'input[name="username"]')
        self.PASSWORD = (By.CSS_SELECTOR, 'input[name="password"]')
        self.SUBMIT = (By.CSS_SELECTOR, 'button[type="submit"]')
        self.ERROR_AREA = (
            By.XPATH,
            '//*[@role="alert"] | //*[@id="slfErrorAlert"] | //div[contains(normalize-space(.), "incorrect")]'
        )
        self.INCORRECT_LOGIN_ERROR_TEXT = (
            By.XPATH,
            '//*[normalize-space(.)="Sorry, your password was incorrect. Please double-check your password."]'
        )

    def expect_loaded(self) -> None:
        """
        Checking if there are some elemeing in the login form
        """
        self.ui_driver.wait_visible(self.ROOT)
        self.ui_driver.wait_visible(self.USERNAME)
        self.ui_driver.wait_visible(self.PASSWORD)

    def login(self, username: str, password: str) -> None:
        """
        Logging in
        """
        self.ui_driver.clear(self.USERNAME)
        self.ui_driver.send_keys(username, self.USERNAME)
        self.ui_driver.clear(self.PASSWORD)
        self.ui_driver.send_keys(password, self.PASSWORD)
        self.ui_driver.click(self.SUBMIT)

    def expect_error_login(self) -> None:
        """
        Verifying if error test is shown when login failed due to incorrect credentials
        """
        log.info("Verifying if error log in text is shown")
        if not self.ui_driver.wait_visible(self.INCORRECT_LOGIN_ERROR_TEXT):
            raise AssertionError(f"self.INCORRECT_LOGIN_ERROR_TEXT element is not visible")
