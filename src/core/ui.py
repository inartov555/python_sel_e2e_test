"""
Selenium driver adapter
"""

from __future__ import annotations
from typing import List

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Ui:
    """
    Selenium driver adapter
    """
    def __init__(self, driver: WebDriver, default_timeout: int = 10) -> None:
        """
        Selenium driver adapter
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, default_timeout)

    def find(self, sel: tuple, root: WebElement = None) -> WebElement:
        """
        Triggers find_element operation
        """
        ctx = root or self.driver
        return ctx.find_element(*sel)

    def finds(self, sel: tuple, root: WebElement = None) -> List[WebElement]:
        """
        Triggers find_elements operation
        """
        ctx = root or self.driver
        return ctx.find_elements(*sel)

    def wait_visible(self, sel: tuple, root: WebElement = None, timeout: int = 15) -> WebElement:
        """
        Waiting till element becomes visible
        """
        if root is None:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(sel))
        elem = WebDriverWait(self.driver, timeout).until(
            lambda d: any(e.is_displayed() for e in root.find_element(*sel)))
        return elem.is_displayed()

    def wait_clickable(self, sel: tuple, timeout: int = 15) -> WebElement:
        """
        Waiting till element becomes clickable
        """
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(sel))

    def wait_for_dom_ready(self, timeout: int = 20) -> None:
        """
        Waiting till page is loaded (DOM is ready)
        """
        WebDriverWait(self.driver, timeout).until(lambda d: d.execute_script("return document.readyState") == "complete")

    def open(self, url, timeout) -> None:
        """
        Opening a URL
        """
        self.driver.get(url)
        self.wait_for_dom_ready(timeout)

    def click(self, sel: tuple, root: WebElement = None) -> WebElement:
        """
        Clicking an element
        """
        ctx = root or self.driver
        elem = ctx.find_element(*sel)
        elem.click()
        return elem

    def clear(self, sel: tuple, root: WebElement = None) -> WebElement:
        """
        Clearing element's text
        """
        ctx = root or self.driver
        elem = ctx.find_element(*sel)
        elem.clear()
        return elem

    def send_keys(self, text: str, sel: tuple, root: WebElement = None) -> WebElement:
        """
        Sending text to an element
        """
        ctx = root or self.driver
        elem = ctx.find_element(*sel)
        elem.send_keys(text)
        return elem

    def execute_script(self, script: str, *args):
        """
        Executing JavaScript code
        """
        return self.driver.execute_script(script, *args)
