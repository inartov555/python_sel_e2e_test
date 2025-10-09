"""
Base methods that can be used by derived pages
"""

from __future__ import annotations

from src.core.app_config import AppConfig
from src.core.ui import Ui
from tools.logger.logger import Logger


log = Logger(__name__)


class BasePage:
    """
    Base methods that can be used by derived pages
    """

    def __init__(self, app_config: AppConfig, uri_path: str, ui_driver: Ui):
        """
        Args:
            app_config (AppConfig): app config passed in ini config file
            uri_path (str): e.g. /accounts/login/
            ui_driver (Ui): selenenium web driver adapter
        """
        self.ui_driver = ui_driver
        self.app_config = app_config
        self.base_url = self.app_config.base_url
        self.uri_path = uri_path
        self.full_url = self.base_url + self.uri_path

    def open(self) -> "BasePage":
        """
        Opening a page
        """
        log.info(f"Opening {self.full_url} URL")
        self.ui_driver.open(self.full_url, 20)
        return self

    def login(self) -> None:
        return None
