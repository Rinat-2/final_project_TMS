import time

from pages.CartPage import CartPageHelper
from pages.DuckPage import DuckPageHelper
from pages.MainPage import MainPageHelper


def test_check_empty_cart(browser):
    main_page = MainPageHelper(browser)
    main_page.open_main_page()
    main_page.click_on_duck()
    duck_page = DuckPageHelper(browser)
    duck_page.add_duck_to_cart()
    duck_page.click_on_cart()
    time.sleep(3)
    cart_page = CartPageHelper(browser)
    cart_page.edit_quantity_ducks()
    cart_page.remove_ducks()
