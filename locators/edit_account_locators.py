from selenium.webdriver.common.by import By


class EditAccountLocators:
    EDIT_ACCOUNT_TEXT = (By.CSS_SELECTOR, 'h1.title')
    FIRST_NAME_FIELD = (By.NAME, 'firstname')
    SAVE_BUTTON = (By.NAME, 'save')
    SUCCESS_CHANGES = (By.CSS_SELECTOR, 'div.notice.success')
