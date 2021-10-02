import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.home_page = "http://127.0.0.1/litecart"

    def open_main_page(self):
        with allure.step('Открываем главную страницу сайта'):
            self.driver.get(self.home_page)
            assert self.driver.title == "Online Store | My Store"

    def find_element(self, locator: tuple, time=20):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Element can't be found by {locator}")

    def click_on_cart(self):
        with allure.step('Открываем корзину'):
            cart = self.driver.find_element(
                By.LINK_TEXT, 'Checkout »')
            cart.click()
