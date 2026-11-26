import pytest
from playwright.sync_api import Page, expect

from pages.inventory_page import InventoryPage


@pytest.mark.regression
def test_end_to_end_checkout(page: Page, logged_in_page: InventoryPage):
    # 1. add product
    logged_in_page.add_to_cart("Sauce Labs Bike Light")
    logged_in_page.cart_link.click()
    #Verify product in cart
    expect(
        page.locator("[data-test='cart-list']")
        .locator("[data-test='inventory-item-name']")
    ).to_have_text("Sauce Labs Bike Light")

    # 2. checkout info
    page.locator("[data-test='checkout']").click()
    page.locator("[data-test='firstName']").fill("Prem")
    page.locator("[data-test='lastName']").fill("Kumar")
    page.locator("[data-test='postalCode']").fill("560001")
    page.locator("[data-test='continue']").click()

    # 3. overview + finish
    expect(page.locator("[data-test='title']")).to_have_text("Checkout: Overview")
    page.locator("[data-test='finish']").click()

    # 4. confirmation
    expect(page.locator("[data-test='complete-header']")).to_have_text(
        "Thank you for your order!"
    )
