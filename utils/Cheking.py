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

    """"Метод для проверки значения полей"""

    @staticmethod
    def chek_json_value(response: Response, field_name, expected_value):
        chek_value = response.json()
        chek_info = chek_value.get(field_name)
        assert chek_info == expected_value
        print(field_name + ' совпадает с эталоном')

        """"Метод для проверки значения по заданному слову"""

    @staticmethod
    def check_json_search_word_in_value(response: Response, field_name, search_word):
        chek_value = response.json()
        chek_info = chek_value.get(field_name)
        if search_word in chek_info:
            print('Слово =' + search_word + ' есть в ответе')
        else:
            print('Слово =' + search_word + ' отсутствует в ответе')
