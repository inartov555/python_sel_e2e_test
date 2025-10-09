from __future__ import annotations

import os
import pytest

pytestmark = pytest.mark.auth

def test_login_and_feed_visible(login_page, home_feed_page, creds):
    if not creds["username"] or not creds["password"]:
        pytest.skip("Provide --username/--password or IG_USERNAME/IG_PASSWORD to run auth test")

    login_page.open()
    login_page.allow_all_cookies_if_shown()
    login_page.expect_loaded()
    login_page.form().login(creds["username"], creds["password"])

    home_feed_page.open()
    home_feed_page.expect_loaded()
