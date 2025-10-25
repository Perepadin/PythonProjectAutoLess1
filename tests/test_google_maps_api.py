import json

from requests import Response
from utils.Cheking import Cheking

from utils.API import Google_Maps_Api

"""Создание / изменение / удаление новой локации"""
class Test_create_place():

    def test_create_new_place(self):

        print('Метод POST')
        # result_post: Response = Google_Maps_Api.create_new_place() #так тоже можно, но это устарело
        result_post = Google_Maps_Api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Cheking.chek_status_code(result_post, 200)
        # token_for_post = json.loads(result_post.text) #получение данных о полях в JSON
        # print(list(token_for_post)) # получение списка полей в JSON
        Cheking.chek_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Cheking.chek_json_value(result_post, 'status', 'OK')

        print('Метод GET после POST')
        result_get = Google_Maps_Api.get_new_place(place_id)
        Cheking.chek_status_code(result_get, 200)
        # token_for_get = json.loads(resulst_get.text) #получение данных о полях в JSON
        # print(list(token_for_get)) # получение списка полей в JSON
        Cheking.chek_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Cheking.chek_json_value(result_get, 'address', '29, side layout, cohen 09')

        print('Метод PUT')
        result_put = Google_Maps_Api.update_new_location(place_id)
        Cheking.chek_status_code(result_put, 200)
        Cheking.chek_json_token(result_put, ['msg'])
        Cheking.chek_json_value(result_put, 'msg', 'Address successfully updated')

        print('Метод GET после PUT')
        result_get = Google_Maps_Api.get_new_place(place_id)
        Cheking.chek_status_code(result_get, 200)
        Cheking.chek_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        print(result_get.text)
        Cheking.chek_json_value(result_get, 'address', "211 Chapova street, RU")

        print('Метод DELETE')
        resulst_delete = Google_Maps_Api.delete_new_location(place_id)
        Cheking.chek_status_code(resulst_delete, 200)
        # token_for_delete = json.loads(resulst_delete.text) #получение данных о полях в JSON
        # print(list(token_for_delete)) # получение списка полей в JSON
        Cheking.chek_json_token(resulst_delete, ['status'])
        Cheking.chek_json_value(resulst_delete, 'status', 'OK')

        print('Метод GET после DELETE')
        result_get = Google_Maps_Api.get_new_place(place_id)
        Cheking.chek_status_code(result_get, 404)
        Cheking.chek_json_token(result_get, ['msg'])
        Cheking.chek_json_value(result_get, 'msg', "Get operation failed, looks like place_id  doesn't exists")
        Cheking.check_json_search_word_in_value(result_get, 'msg', 'failed')

        print("Тестирование создания / изменения / удаления новой локации - проведено успешно")

        # print('Метод PUT Для теста')
        # resulst_put_test= Google_Maps_Api.update_test_location(self)


