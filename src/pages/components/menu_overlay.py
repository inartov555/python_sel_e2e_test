"""
Represents the menu pane in the home page.
"""

from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from tools.logger.logger import Logger
from src.pages.base_page import BasePage
from src.pages.components.base_component import BaseComponent


log = Logger(__name__)


class MenuOverlay(BaseComponent):
    """
    Represents the menu pane in the home page.
    """

    def __init__(self, ui_driver: Ui, web_elem: WebElement = None):
        """
        Args:
            ui_driver (Ui): selenenium web driver adapter
        """
        super().__init__(ui_driver, web_elem)
        self.LOGOUT_ELEM = (
            By.XPATH,
            './/*[normalize-space(.)="Log out"]/ancestor::*[@role="button"][1]'
        )
        self.LOGGING_OUT_TEXT = (
            By.XPATH,
            './/*[normalize-space(.)="Logging out"]'
        )

    def log_out(self) -> None:
        """
        Logging out
        """
        log.info("Logging out")
        self.ui_driver.wait_visible(self.LOGOUT_ELEM)
        self.ui_driver.click(self.LOGOUT_ELEM)
        self.ui_driver.wait_visible(self.LOGGING_OUT_TEXT)

    def is_open(self) -> bool:
        """
        Check if it's open
        """
        return None
