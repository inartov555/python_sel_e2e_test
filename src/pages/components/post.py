"""
Represents a post in the home page.
Some elements do not support regular click, that's why JS click event was dispatched for them.
"""

from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.core.ui import Ui
from src.pages.components.base_component import BaseComponent


class PostCard(BaseComponent):
    """
    Represents a post in the home page.
    Some elements do not support regular click, that's why JS click event was dispatched for them.
    """

    def __init__(self, ui_driver: Ui, web_elem: WebElement):
        """
        Args:
            ui_driver (Ui): selenenium web driver adapter
            web_elem (WebElement): it's needed only if you 
        """
        super().__init__(ui_driver, web_elem)
        self.like_button = (By.XPATH, '//div[@role="button"][.//svg[@aria-label="Like"]]')
        self.unlike_button = (By.XPATH, '//div[@role="button"][.//svg[@aria-label="Unlike"]]')
        self.save_button = (By.XPATH, '//div[@role="button"][.//svg[@aria-label="Save"]]')
        self.remove_button = (By.XPATH, '//div[@role="button"][.//svg[@aria-label="Remove"]]')
        self.comment_button = (By.XPATH, '//div[@role="button"][.//svg[@aria-label="Comment"]]')
        self.liked_by_link = (By.CSS_SELECTOR, 'a[href*="/liked_by/"]')

    def scroll_to_element_liked_by(self) -> None:
        """
        Scrolling to an element liked by users
        """
        el = self.ui_driver.find(self.liked_by_link, self.web_elem)
        self.ui_driver.execute_script(
            "arguments[0].scrollIntoView({block:'center', inline:'nearest'});", el
        )

    def like(self) -> None:
        """
        Liking a post
        """
        # expect(self.like_button).to_be_visible(); dispatch_event('click'); expect(unlike).to_be_visible()
        self.ui_driver.click(self.like_button, self.web_elem)
        self.ui_driver.wait_visible(self.unlike_button, self.web_elem)

    def unlike(self) -> None:
        """
        Unliking a post
        """
        self.ui_driver.click(self.unlike_button, self.web_elem)
        self.ui_driver.wait_visible(self.like_button, self.web_elem)

    def save(self) -> None:
        """
        Saving a post
        """
        self.ui_driver.click(self.save_button, self.web_elem)
        self.ui_driver.wait_visible(self.remove_button, self.web_elem)

    def remove(self) -> None:
        """
        Removing a post from saved ones
        """
        self.ui_driver.click(self.remove_button, self.web_elem)
        self.ui_driver.wait_clickable(self.save_button, self.web_elem)

    def open_comments(self) -> None:
        """
        Open the comments
        """
        self.ui_driver.click(self.comment_button, self.web_elem)

    def expect_comment_button_visible(self) -> None:
        """
        Checking if the comment button is visible
        """
        self.ui_driver.wait_visible(self.comment_button, self.web_elem)
