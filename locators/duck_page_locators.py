from selenium.webdriver.common.by import By


class DuckPageLocators:
    DROPDOWN_LIST_BUTTON = (By.NAME, 'options[Size]')
    VALUE_IN_DROPDOWN_LIST = (By.XPATH, '//option[@value="Small"]')
    ADD_TO_CART_BUTTON = (By.NAME, 'add_cart_product')
    CARD_QUANTITY_TEXT = (By.CSS_SELECTOR, 'span.quantity')
