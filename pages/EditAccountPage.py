import allure

from locators.edit_account_locators import EditAccountLocators
from pages.BasePage import BasePage


class EditAccountPageHelper(BasePage):

    def set_first_name(self, first_name):
        with allure.step('Вводим имя'):
            first_name_field = self.find_element(
                EditAccountLocators.FIRST_NAME_FIELD)
            first_name_field.click()
            first_name_field.clear()
            first_name_field.send_keys(first_name)

    def click_on_save_button(self):
        with allure.step('Нажимаем на кнопку сохранения'):
            save_button = self.find_element(
                EditAccountLocators.SAVE_BUTTON)
            save_button.click()
            success_changes = self.find_element(
                EditAccountLocators.SUCCESS_CHANGES)
            assert success_changes.is_displayed()
