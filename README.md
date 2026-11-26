# Playwright Python Test Automation Project

UI test framework using **Playwright + pytest** with the **Page Object Model**.
Target app: https://www.saucedemo.com (public demo site).

## Project structure

```
playwright_project/
├── conftest.py            # shared fixtures
├── pytest.ini             # pytest + playwright options, markers
├── requirements.txt
├── .env.example           # copy to .env to override config
├── pages/                 # page objects (locators + actions)
│   ├── base_page.py
│   ├── login_page.py
│   └── inventory_page.py
├── tests/                 # test cases
│   ├── test_login.py
│   ├── test_inventory.py
│   └── test_checkout_e2e.py
├── utils/config.py        # env-based configuration
└── .github/workflows/playwright.yml   # CI
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install               # downloads browsers
cp .env.example .env             # optional
```

## Run

```bash
pytest                                   # all tests, headless chromium
pytest --headed --slowmo 500             # watch the browser
pytest -m smoke                          # only smoke tests
pytest tests/test_login.py::test_valid_login
pytest --browser firefox --browser webkit  # cross-browser
pytest -n 4                              # parallel (pytest-xdist)
```

## Outputs

- HTML report: `reports/report.html`
- Screenshots, videos, traces on failure: `test-results/`
- Open a trace: `playwright show-trace test-results/<test>/trace.zip`

## Generate locators quickly

```bash
playwright codegen https://www.saucedemo.com
```
