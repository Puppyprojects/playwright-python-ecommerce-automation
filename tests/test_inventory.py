import pytest
from playwright.sync_api import expect

from pages.inventory_page import InventoryPage


@pytest.mark.smoke
@pytest.mark.inventory
def test_six_products_displayed(logged_in_page: InventoryPage):
    expect(logged_in_page.items).to_have_count(6)


@pytest.mark.regression
@pytest.mark.inventory
def test_add_and_remove_item(logged_in_page: InventoryPage):
    logged_in_page.add_to_cart("Sauce Labs Backpack")
    expect(logged_in_page.cart_badge).to_have_text("1")

    logged_in_page.remove_from_cart("Sauce Labs Backpack")
    expect(logged_in_page.cart_badge).to_have_count(0)


@pytest.mark.regression
@pytest.mark.inventory
def test_sort_price_low_to_high(logged_in_page: InventoryPage):
    logged_in_page.sort_by("lohi")
    prices = logged_in_page.get_prices()
    assert prices == sorted(prices)


@pytest.mark.regression
@pytest.mark.inventory
def test_sort_name_z_to_a(logged_in_page: InventoryPage):
    logged_in_page.sort_by("za")
    names = logged_in_page.get_names()
    assert names == sorted(names, reverse=True)
