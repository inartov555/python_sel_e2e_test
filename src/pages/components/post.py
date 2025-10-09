from __future__ import annotations

from selenium.webdriver.common.by import By

class PostLocators:
    CONTAINER = (By.XPATH, '//article')
    LIKE_BTN = (By.XPATH, './/div[@role="button"][.//svg[@aria-label="Like"]]')
    UNLIKE_BTN = (By.XPATH, './/div[@role="button"][.//svg[@aria-label="Unlike"]]')
    SAVE_BTN = (By.XPATH, './/div[@role="button"][.//svg[@aria-label="Save"]]')
    COMMENT_BTN = (By.XPATH, './/div[@role="button"][.//svg[@aria-label="Comment"]]')
    LIKED_BY_LINK = (By.CSS_SELECTOR, 'a[href*="/liked_by/"]')
