from __future__ import annotations

import pytest

def test_landing_page_loads(landing_page):
    landing_page.open()
    landing_page.accept_cookies_if_shown()
    landing_page.expect_loaded()

def test_login_page_elements(login_page):
    login_page.open()
    login_page.allow_all_cookies_if_shown()
    login_page.expect_loaded()

def test_signup_page_elements(signup_page):
    signup_page.open()
    signup_page.accept_cookies_if_shown()
    signup_page.expect_loaded()

def test_login_negative_incorrect_creds(login_page):
    login_page.open()
    login_page.allow_all_cookies_if_shown()
    login_page.expect_loaded()
    form = login_page.form()
    form.login("invalid_user_123456", "wrong_password_123")
    errs = form.ui.finds(form.ERROR_AREA)
    assert errs is not None

def test_cookie_banner_optional(landing_page):
    landing_page.open()
    _ = landing_page.accept_cookies_if_shown()
