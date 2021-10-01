from db_connections import DbConnectionHelper
from pages.EditAccountPage import EditAccountPageHelper
from pages.MainPage import MainPageHelper


def test_edit_account_username(browser, first_name='Admin'):
    main_page = MainPageHelper(browser)
    main_page.open_main_page()
    main_page.set_email_adress()
    main_page.set_password()
    main_page.click_on_login_button()
    main_page.click_on_edit_account()
    edit_account_page = EditAccountPageHelper(browser)
    edit_account_page.set_first_name(first_name)
    edit_account_page.click_on_save_button()
    db_connection = DbConnectionHelper()
    db_connection.check_username_changed()

