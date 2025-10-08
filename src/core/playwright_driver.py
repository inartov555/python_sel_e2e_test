# TODO(SELENIUM): Convert Playwright role/text queries to By.XPATH or By.CSS_SELECTOR.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest

"""
The adapter for the Playwright driver
"""

from typing import Optional

from src.core.ui_driver import UIDriver, WaitState
from src.core.app_config import AppConfig


class PlaywrightDriver(UIDriver):
    """
    The adapter for the Playwright driver
    """
    def __init__(self, app_config: AppConfig, driver: Page) -> None:
        """
        app_config (AppConfig): app config from ini config file
        driver (Page): playwright driver object
        """
        self.driver = driver
        self.app_config = app_config

    def _timeout(self, t: Optional[int]) -> int:
        """
        Timeout
        """
        return t if t is not None else self.app_config.action_timeout

    def goto(self, url: str, wait_until: str, timeout: int) -> None:
        """
        Go to a driver
        """
        self.driver.get(url, wait_until=wait_until, timeout=timeout)

    def click(self, sel: str, timeout_ms: Optional[int] = None) -> None:
        """
        Click a locator
        """
        self.driver.locator(sel).click(timeout=self._timeout(timeout_ms))

    def type(self, sel: str, text: str, delay_ms: Optional[int] = None, timeout_ms: Optional[int] = None) -> None:
        """
        Type some text in a locator
        """
        loc = self.driver.locator(sel)
        # Consistent behavior: start clean
        loc.fill("", timeout=self._timeout(timeout_ms))
        loc.type(text, delay=delay_ms, timeout=self._timeout(timeout_ms))

    def fill(self, sel: str, text: str, timeout_ms: Optional[int] = None) -> None:
        """
        Fill in a locator with text
        """
el = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "sel")))
el.clear()
el.send_keys(text, timeout=self._timeout(timeout_ms)

    def text(self, sel: str, timeout_ms: Optional[int] = None) -> str:
        """
        Get inner locator's text
        """
        loc = self.driver.locator(sel)
        # Ensure at least one match (better error than inner_text on empty set)
        if loc.count() == 0:
            raise AssertionError(f"No elements match selector: {sel}")
        return loc.first.inner_text(timeout=self._timeout(timeout_ms)).strip()

    def is_visible(self, sel: str, timeout_ms: Optional[int] = None) -> bool:
        """
        Is a locator visible
        """
        return self.driver.locator(sel).is_visible(timeout=self._timeout(timeout_ms))

    def wait_for(self, sel: str, state: WaitState = "visible", timeout_ms: Optional[int] = None) -> None:
        """
        Wait for locator
        """
        self.driver.locator(sel).wait_for(state=state, timeout=self._timeout(timeout_ms))

    def screenshot(self, path: str, full_page: bool = True) -> None:
        """
        Take a screenshot
        """
        self.driver.screenshot(path=path, full_page=full_page, timeout=self.app_config.action_timeout)

    def attr(self, sel: str, name: str, timeout_ms: Optional[int] = None) -> Optional[str]:
        """
        Get locator attribute
        """
        return self.driver.locator(sel).get_attribute(name, timeout=self._timeout(timeout_ms))

    def count(self, sel: str, timeout_ms: Optional[int] = None) -> int:
        """
        Playwright doesn't expose timeout on count(); do an existence wait first
        """
        self.driver.locator(sel).first.wait_for(state="attached", timeout=self._timeout(timeout_ms))
        return self.driver.locator(sel).count()

    def wait_for_function(self, js_code: str, timeout: int) -> None:
        """
        Wait for JavaScript function to finish
        """
        self.driver.wait_for_function(js_code, timeout=timeout)

    def locator(self, loc: str) -> Locator:
        """
        Get locator
        """
        return self.driver.locator(loc)

    def get_by_text(self, text: str) -> Locator:
        """
        Get element by text
        """
        return self.driver.get_by_text(text)