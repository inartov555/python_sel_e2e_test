from __future__ import annotations

from selenium.webdriver.remote.webdriver import WebDriver
from src.core.ui import Ui

class BasePage:
    BASE_URL = "https://www.instagram.com"

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.ui = Ui(driver)

    @property
    def path(self) -> str:
        return "/"

    @property
    def url(self) -> str:
        return f"{self.BASE_URL}{self.path}"

    def open(self) -> None:
        self.driver.get(self.url)
        self.ui.wait_for_dom_ready()
