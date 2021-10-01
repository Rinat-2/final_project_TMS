import allure

from locators.edit_account_locators import EditAccountLocators
from locators.main_page_locators import MainPageLocators
from pages.BasePage import BasePage


class MainPageHelper(BasePage):

    def set_email_adress(self):
        with allure.step('Вводим email'):
            email_field = self.find_element(
                MainPageLocators.EMAIL_ADRESS_FIELD)
            email_field.send_keys('admin@gmail.com')

    def set_password(self):
        with allure.step('Вводим пароль'):
            password_field = self.find_element(
                MainPageLocators.PASSWORD_FIELD)
            password_field.send_keys('admin')

    def click_on_login_button(self):
        with allure.step('Нажимаем на кнопку Login'):
            login_button = self.find_element(
                MainPageLocators.LOGIN_BUTTON)
            login_button.click()
            success_notice = self.find_element(
                MainPageLocators.SUCCESS_LOGIN_NOTICE)
            assert success_notice.is_displayed()

    def click_on_edit_account(self):
        with allure.step('Нажимаем на гипертекст Edit account'):
            edit_account = self.find_element(
                MainPageLocators.EDIT_ACCOUNT_LINK_TEXT)
            edit_account.click()
            edit_account_text = self.find_element(
                EditAccountLocators.EDIT_ACCOUNT_TEXT).text
            assert edit_account_text == 'Edit Account'

    def click_on_duck(self):
        with allure.step('Нажимаем на утку'):
            click_on_duck = self.find_element(
                MainPageLocators.CLICK_ON_DUCK)
            click_on_duck.click()
