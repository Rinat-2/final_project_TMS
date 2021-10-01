import time

import allure

from locators.duck_page_locators import DuckPageLocators
from pages.BasePage import BasePage


class DuckPageHelper(BasePage):

    def add_duck_to_cart(self):
        with allure.step('Добавляем уточку в корзину'):
            size_button = self.find_element(
                DuckPageLocators.DROPDOWN_LIST_BUTTON)
            size_button.click()
            size_option = self.find_element(
                DuckPageLocators.VALUE_IN_DROPDOWN_LIST)
            size_option.click()
            add_to_cart = self.find_element(
                DuckPageLocators.ADD_TO_CART_BUTTON)
            add_to_cart.click()
            time.sleep(3)
            card_quantity = self.find_element(
                DuckPageLocators.CARD_QUANTITY_TEXT)
            assert card_quantity.text == '1'
