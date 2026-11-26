import pytest
from playwright.sync_api import Page

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils import config


@pytest.fixture(scope="session")
def base_url():
    # pytest-playwright uses this fixture so page.goto("/") works
    return config.BASE_URL


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1366, "height": 768},
        "ignore_https_errors": True,
    }


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    lp = LoginPage(page)
    lp.load()
    return lp


@pytest.fixture
def logged_in_page(page: Page, login_page: LoginPage) -> InventoryPage:
    """Logs in with the standard user and returns the inventory page object."""
    login_page.login(config.STANDARD_USER, config.PASSWORD)
    return InventoryPage(page)
