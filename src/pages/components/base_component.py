"""
Base methods for derived components
"""

from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from src.core.ui import Ui

from tools.logger.logger import Logger


log = Logger(__name__)


class BaseComponent:
    """
    Base methods for derived components
    """
    def __init__(self, ui_driver: Ui, web_elem: WebElement = None):
        """
        Args:
            ui_driver (Ui): selenenium web driver adapter
            web_elem (WebElement): web element
        """
        self.ui_driver = ui_driver
        self.web_elem = web_elem

    def is_visible(self) -> bool:
        """
        Check if element is visible
        """
        return None  # TO BE DONE

    def wait_for_hidden(self) -> None:
        """
        Wait for element to be hidden
        """
        return None  # TO BE DONE
