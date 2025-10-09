"""
Cookie banner
"""

from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.core.ui import Ui
from src.pages.components.base_component import BaseComponent


class CookieBanner(BaseComponent):
    """
    Cookie banner
    """

    def __init__(self, ui_driver: Ui, web_elem: WebElement = None):
        """
        Args:
            ui_driver (Ui): selenenium web driver adapter
            web_elem (WebElement): web element
        """
        super().__init__(ui_driver, web_elem)
        self.ALLOW_ALL = (By.CSS_SELECTOR, 'button._a9--._ap36._asz1')

    def accept_if_present(self) -> bool:
        """
        Accepting cookie banner, if shown
        """
        elem = self.ui_driver.find(self.ALLOW_ALL)
        if elem:
            try:
                if elem.is_displayed():
                    elem.click()
                    return True
            except Exception:
                pass
        return False
