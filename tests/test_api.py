import json
import time

import allure
import requests


def test_check_changes_username():
    with allure.step('Создаем пользователя'):
        with open('C://Users/rinat/PycharmProjects'
                  '/final_project_TMS/data/user.json',
                  encoding='utf-8') as f:
            user_info = json.loads(f.read())
        create_user_url = 'https://petstore.swagger.io/v2/user'
        response = requests.post(create_user_url, json=user_info)
        time.sleep(1)
        assert response.status_code == 200

    with allure.step('Проверяем данные пользователя'):
        user_url = 'https://petstore.swagger.io/v2/user/Rinat'
        response = requests.get(user_url)
        assert response.status_code == 200

    with allure.step('Изменяем данные пользователя'):
        with open('C://Users/rinat/PycharmProjects'
                  '/final_project_TMS/data/updated_user.json',
                  encoding='utf-8') as f:
            updated_user = json.loads(f.read())
            response = requests.put(user_url, json=updated_user)
            assert response.status_code == 200
