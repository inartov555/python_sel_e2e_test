from __future__ import annotations

from typing import Tuple, List
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Locator = Tuple[str, str]

class Ui:
    def __init__(self, driver: WebDriver, default_timeout: int = 10) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, default_timeout)

    def find(self, locator: Locator, root: WebElement | None = None) -> WebElement:
        ctx = root or self.driver
        return ctx.find_element(*locator)

    def finds(self, locator: Locator, root: WebElement | None = None) -> List[WebElement]:
        ctx = root or self.driver
        return ctx.find_elements(*locator)

    def wait_visible(self, locator: Locator, timeout: int | None = None, root: WebElement | None = None) -> WebElement:
        if root is None:
            return WebDriverWait(self.driver, timeout or self.wait._timeout).until(EC.visibility_of_element_located(locator))
        WebDriverWait(self.driver, timeout or self.wait._timeout).until(lambda d: any(e.is_displayed() for e in root.find_elements(*locator)))
        return next(e for e in root.find_elements(*locator) if e.is_displayed())

    def wait_clickable(self, locator: Locator, timeout: int | None = None) -> WebElement:
        return WebDriverWait(self.driver, timeout or self.wait._timeout).until(EC.element_to_be_clickable(locator))

    def wait_for_dom_ready(self, timeout: int = 20) -> None:
        WebDriverWait(self.driver, timeout).until(lambda d: d.execute_script("return document.readyState") == "complete")
