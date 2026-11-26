import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from utils import config


@pytest.mark.smoke
@pytest.mark.login
def test_login_page_title(login_page: LoginPage, page: Page):
    expect(page).to_have_title("Swag Labs")
    expect(login_page.login_button).to_be_visible()


@pytest.mark.smoke
@pytest.mark.login
def test_valid_login(login_page: LoginPage, page: Page):
    login_page.login(config.STANDARD_USER, config.PASSWORD)
    expect(page).to_have_url(f"{config.BASE_URL}/inventory.html")
    expect(page.locator("[data-test='title']")).to_have_text("Products")


@pytest.mark.regression
@pytest.mark.login
def test_locked_out_user(login_page: LoginPage):
    login_page.login(config.LOCKED_USER, config.PASSWORD)
    expect(login_page.error_message).to_contain_text("locked out")


@pytest.mark.regression
@pytest.mark.login
@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("", "", "Username is required"),
        ("standard_user", "", "Password is required"),
        ("wrong_user", "wrong_pass", "do not match"),
    ],
)
def test_invalid_login(login_page: LoginPage, username, password, expected_error):
    login_page.login(username, password)
    expect(login_page.error_message).to_contain_text(expected_error)
