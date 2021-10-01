from selenium.webdriver.common.by import By


class CartPageLocators:
    QUANTITY_NUMBER_TEXT = (
        By.XPATH, '//table[@class="dataTable rounded-corners"]'
                  '/tbody/tr[2]/td')
    UPDATE_BUTTON = (By.NAME, 'update_cart_item')
    TOTAL_SUM_TEXT = (By.XPATH, '//td[@class="sum"]')
    REMOVE_BUTTON = (By.NAME, 'remove_cart_item')
    EMPTY_CART_TEXT = (
        By.XPATH, '//div[@id="checkout-cart-wrapper"]/p/em')
