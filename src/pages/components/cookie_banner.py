from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from src.core.ui import Ui

class CookieBanner:
    ALLOW_ALL = (By.CSS_SELECTOR, 'button._a9--._ap36._asz1')

    def __init__(self, driver: WebDriver) -> None:
        self.ui = Ui(driver)

    def accept_if_present(self) -> bool:
        els = self.ui.finds(self.ALLOW_ALL)
        if els:
            try:
                if els[0].is_displayed():
                    els[0].click()
                    return True
            except Exception:
                pass
        return False
