import allure
import mysql.connector


class DbConnectionHelper:

    def check_username_changed(self):
        with allure.step('Проверяем имя в базе'):
            connection = mysql.connector.connect(host='127.0.0.1',
                                                 database='litecart',
                                                 user='root',
                                                 password='')

            try:
                cursor = connection.cursor()
                cursor.execute('select username from lc_users')
                username = cursor.fetchall()
                new_username = 'admin'
                for i in username[0]:
                    if i == new_username:
                        assert True
                    else:
                        assert False
            finally:
                connection.close()
