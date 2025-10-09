from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from src.core.ui import Ui

class LoginForm:
    ROOT = (By.CSS_SELECTOR, "form#loginForm")
    USERNAME = (By.CSS_SELECTOR, 'input[name="username"]')
    PASSWORD = (By.CSS_SELECTOR, 'input[name="password"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[type="submit"]')
    ERROR_AREA = (
        By.XPATH,
        '//*[@role="alert"] | //*[@id="slfErrorAlert"] | //div[contains(normalize-space(.), "incorrect")]'
    )

    def __init__(self, driver: WebDriver) -> None:
        self.ui = Ui(driver)

    def expect_loaded(self) -> None:
        self.ui.wait_visible(self.ROOT)
        self.ui.wait_visible(self.USERNAME)
        self.ui.wait_visible(self.PASSWORD)

    def login(self, username: str, password: str) -> None:
        self.ui.wait_visible(self.USERNAME).clear()
        self.ui.find(self.USERNAME).send_keys(username)
        self.ui.find(self.PASSWORD).clear()
        self.ui.find(self.PASSWORD).send_keys(password)
        self.ui.find(self.SUBMIT).click()
