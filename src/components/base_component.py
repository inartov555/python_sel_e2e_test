from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


"""
Base methods for derived components
"""

from __future__ import annotations

from tools.logger.logger import Logger
from src.pages.base_page import BasePage

log = Logger(__name__)

class BaseComponent:
    """
    Base methods for derived components
    """
    def __init__(self, root: Locator, page_class: BasePage):
        """
        Args:
            root (Locator): locator
            page_clas (BasePage): a driver derived from BasePage
        """
        self.root = root
        self.page_class = page_class

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