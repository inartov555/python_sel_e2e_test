# Instagram E2E (Selenium + Pytest) — Test Assignment

This project demonstrates SOLID/OOP Page Objects for Instagram (desktop, FullHD) using Selenium 4 + Pytest.

## How to run
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -q                   # public tests
pytest -q --headed          # headed
pytest -q --browser=firefox # choose browser
pytest -q -m auth --username "USER" --password "PASS"  # authenticated (optional)
```
> Auth tests may fail due to CAPTCHA; the focus is code quality.

## Design
- Page Object pattern with components (`LoginForm`, `CookieBanner`, `Post`).
- Explicit waits via `WebDriverWait + EC`, wrapped in `Ui` helper.
- Selectors prefer attributes/ARIA to be locale-agnostic.
