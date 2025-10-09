from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.pages.base_page import BasePage
from src.pages.components.post import PostLocators

class HomeFeedPage(BasePage):
    @property
    def path(self) -> str:
        return "/"

    HOME_TAB = (By.XPATH, "//a[@href='/?next=%2F' or @href='/']")
    MENU_MORE = (By.XPATH, "//*[normalize-space(.)='More']/ancestor::a[@role='link'][1]")

    def expect_loaded(self) -> None:
        self.ui.wait_for_dom_ready()
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(PostLocators.CONTAINER))

    def first_post_container(self):
        return self.ui.find(PostLocators.CONTAINER)

    def like_first_post_if_possible(self) -> bool:
        post = self.first_post_container()
        try:
            btns = post.find_elements(*PostLocators.LIKE_BTN)
            if btns:
                btns[0].click()
                return True
        except Exception:
            pass
        return False
