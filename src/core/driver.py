from __future__ import annotations

from typing import Tuple, Optional
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.remote.webdriver import WebDriver

def build_driver(
    browser: str = "chrome",
    window_size: Tuple[int, int] = (1920, 1080),
    headless: bool = True,
    chromium_binary: Optional[str] = None,
) -> WebDriver:
    w, h = window_size
    b = browser.lower()

    if b in ("chrome", "chromium"):
        opts = ChromeOptions()
        if headless:
            opts.add_argument("--headless=new")
        opts.add_argument(f"--window-size={w},{h}")
        opts.add_argument("--no-sandbox")
        opts.add_argument("--disable-dev-shm-usage")
        if b == "chromium" and chromium_binary:
            opts.binary_location = chromium_binary
        return webdriver.Chrome(options=opts)

    if b == "msedge":
        opts = EdgeOptions()
        if headless:
            opts.add_argument("--headless=new")
        opts.add_argument(f"--window-size={w},{h}")
        return webdriver.Edge(options=opts)

    if b == "firefox":
        opts = FirefoxOptions()
        if headless:
            opts.add_argument("-headless")
        drv = webdriver.Firefox(options=opts)
        drv.set_window_size(w, h)
        return drv

    if b in ("safari", "webkit"):
        opts = SafariOptions()
        drv = webdriver.Safari(options=opts)
        drv.set_window_size(w, h)
        return drv

    raise ValueError(f"Unsupported browser: {browser}")
