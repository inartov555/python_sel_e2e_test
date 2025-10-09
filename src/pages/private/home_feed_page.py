"""
Authorized Home page
"""

from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tools.logger.logger import Logger
from src.pages.components.menu_overlay import MenuOverlay
from src.pages.components.post import PostCard
from src.core.app_config import AppConfig
from src.core.ui import Ui
from src.pages.base_page import BasePage


log = Logger(__name__)


class HomeFeedPage(BasePage):
    """
    Authorized Home page
    """
    def __init__(self, app_config: AppConfig, ui_driver: Ui):
        """
        / - URI path

        Args:
            app_config (AppConfig): app config passed in ini config file
            ui_driver (Ui): selenenium web driver adapter
        """
        super().__init__(app_config, "/", ui_driver)
        self.home_tab = (By.XPATH, "//a[@href='/?next=%2F' or @href='/']")
        self.menu_more = (By.XPATH, "//*[normalize-space(.)='More']/ancestor::a[@role='link'][1]")
        self.post_container   = (By.CSS_SELECTOR, "article")
        self.menu_overlay_root = (By.CSS_SELECTOR, 'div[role="dialog"]')

    @property
    def first_post(self) -> PostCard:
        """
        Get the 1st post (Selenium: the wait returns the first matching WebElement)
        """
        result = None
        if self.posts:
            result = self.posts[0]
        return result

    @property
    def posts(self) -> list[PostCard]:
        """
        Get all currently loaded posts
        """
        # Ensure at least one is present before grabbing the list
        WebDriverWait(self.ui_driver.driver, 10).until(
            EC.presence_of_element_located(self.post_container)
        )
        elements = self.ui_driver.finds(self.post_container)
        if elements:
            visible_posts = [PostCard(self.ui_driver, elem) for elem in elements]
        else:
            visible_posts = []
        return visible_posts

    @property
    def menu_overlay(self) -> MenuOverlay:
        """
        Get the 'More' overlay root
        """
        root = WebDriverWait(self.ui_driver.driver, 10).until(
            EC.presence_of_element_located(self.menu_overlay_root)
        )
        return MenuOverlay(self.ui_driver, root)

    def go_to_home_tab(self) -> None:
        """
        Call this method only if the Home tab is not focused
        """
        WebDriverWait(self.ui_driver.driver, 10).until(
            EC.element_to_be_clickable(self.home_tab)
        ).click()

    def open_menu_overlay(self) -> None:
        """
        Open the 'More' overlay
        """
        WebDriverWait(self.ui_driver.driver, 10).until(
            EC.element_to_be_clickable(self.menu_more)
        ).click()

    def expect_home_tab_visible(self) -> None:
        """
        Check if the Home tab is visible
        """
        WebDriverWait(self.ui_driver.driver, 10).until(
            EC.visibility_of_element_located(self.home_tab)
        )

    def expect_feed_visible(self) -> None:
        """
        Check if the 1st post is visible
        """
        WebDriverWait(self.ui_driver.driver, 10).until(
            EC.visibility_of_element_located(self.post_container)
        )
