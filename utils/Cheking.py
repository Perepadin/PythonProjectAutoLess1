import json
import requests
from requests import Response

""""Методы для проверки ответов запросов"""

class Cheking():


    """"Метод для проверки статус кода запросов"""
    @staticmethod
    def chek_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print('Статус код ='  + str(response.status_code))
        else:
            print('Статус код не равен ' + str(response.status_code))


    """"Метод для проверки наличия обязательных полей"""

    @staticmethod
    def chek_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print('Все поля на месте')

