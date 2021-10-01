from selenium.webdriver.common.by import By


class MainPageLocators:
    EMAIL_ADRESS_FIELD = (By.NAME, 'email')
    PASSWORD_FIELD = (By.NAME, 'password')
    LOGIN_BUTTON = (By.NAME, 'login')
    SUCCESS_LOGIN_NOTICE = (By.CSS_SELECTOR, 'div.notice.success')
    EDIT_ACCOUNT_LINK_TEXT = (By.LINK_TEXT, 'Edit Account')
    CLICK_ON_DUCK = (
        By.XPATH, '//div[@id="box-campaigns"]/div/ul/li/a[1]')
