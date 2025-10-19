from requests import Response

from utils.API import Google_Maps_Api

"""Создание / изменение / удаление новой локации"""
class Test_create_place():
    def test_create_new_place(self):

        print('Метод POST')
        # result_post: Response = Google_Maps_Api.create_new_place() #так тоже можно, но это устарело
        result_post = Google_Maps_Api.create_new_place()

        check_post = result_post.json()
        place_id = check_post.get("place_id")


        print('Метод GET')
        resulst_get = Google_Maps_Api.get_new_place(place_id)

        print('Метод PUT')
        result_put = Google_Maps_Api.update_new_location(place_id)

        print('Метод GET после PUT')
        resulst_get = Google_Maps_Api.get_new_place(place_id)
