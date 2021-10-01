import time

from locators.cart_page_locator import CartPageLocators
from pages.BasePage import BasePage


class CartPageHelper(BasePage):
    def edit_quantity_ducks(self):
        self.driver.execute_script(
            f'document.getElementsByName('
            f'"quantity")[0].setAttribute("value" , "3")')
        update_button = self.find_element(CartPageLocators.UPDATE_BUTTON)
        update_button.click()
        time.sleep(3)
        ducks_quantity = self.find_element(
            CartPageLocators.QUANTITY_NUMBER_TEXT)
        total_sum = self.find_element(CartPageLocators.TOTAL_SUM_TEXT)
        assert ducks_quantity.text == '3'
        assert total_sum.text == '$54.00'

    def remove_ducks(self):
        remove_button = self.find_element(CartPageLocators.REMOVE_BUTTON)
        remove_button.click()
        no_item = self.find_element(CartPageLocators.EMPTY_CART_TEXT)
        assert no_item.text == 'There are no items in your cart.'
