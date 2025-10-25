from utils.http_method import Http_method

""""Методы для тестирования Google Maps"""

base_url = 'https://rahulshettyacademy.com' # базовый URL
key = '?key=qaclick123' # базовый параметр для всех запросов
class Google_Maps_Api():
    """"Метод создания новой локации"""
    @staticmethod
    def create_new_place():
        json_for_create_new_location =\
        {
        "location": {
        "lat": -44.383494,
        "lng": 44.427362
        },
        "accuracy": 50,
        "name": "Frontline house",
        "phone_number": "(+91)777 893 3937",
        "address": "29, side layout, cohen 09",
        "types": [
        "shoe park",
        "shop"
        ],
        "website": "http://google.com",
        "language": "French-IN"
        }
        Post_Resource_Url = '/maps/api/place/add/json'  # ресурс для всех POST запросов

        Post_Url = base_url + Post_Resource_Url + key
        print(Post_Url)

        Result_Post = Http_method.custom_post_method(Post_Url, json_for_create_new_location)
        print(Result_Post.text)
        return Result_Post

    """"Метод получения новой локации"""
    @staticmethod
    def get_new_place(place_id):
        Get_resource_url = '/maps/api/place/get/json'  # ресурс для всех GET запросов
        Get_Url = base_url + Get_resource_url + key + "&place_id=" + place_id
        # Get_Url = base_url + Get_resource_url + key + f'{place_id}'
        print(Get_Url)

        Result_Get = Http_method.custom_get_method(Get_Url)
        print(Result_Get.text)
        return Result_Get

    """метод изменения новой локации через PUT"""
    @staticmethod
    def update_new_location(place_id):

        Put_resource_url = '/maps/api/place/update/json'  # ресурс для всех PUT запросов
        Put_url = base_url + Put_resource_url + key
        print(Put_url)
        json_for_update_location = \
            {
                "place_id": place_id,
                "address": "777 Lenina street, RU",
                "key": "qaclick123"
            }
        result_put = Http_method.custom_put_method(Put_url, json_for_update_location)
        print(result_put.text)
        return result_put

    """метод для удаления новой локации через DELETE"""
    @staticmethod
    def delete_new_location(place_id):

        delete_resource_url = '/maps/api/place/delete/json'  # приставка для всех DELETE запросов
        delete_url = base_url + delete_resource_url + key
        print(delete_url)
        json_for_delete_location = \
            {
                "place_id": place_id
            }
        result_delete = Http_method.custom_delete_method(delete_url, json_for_delete_location)
        print(result_delete.text)
        return result_delete










    # def update_test_location(self):
    #     url = 'https://petstore.swagger.io/v2/pet'
    #     print(url)
    #     json_put = [
    #         {
    #             "id": 1,
    #             "category": {
    #                 "id": 1,
    #                 "name": "Bobik"
    #             },
    #             "name": "doggie",
    #             "photoUrls": [
    #                 "string"
    #             ],
    #             "tags": [
    #                 {
    #                     "id": "1",
    #                     "name": "Bob"
    #                 }
    #             ],
    #             "status": "available"
    #         }
    #     ]
    #     result_test_put = Http_method.update_test_location(url, json_put)
    #     print(result_test_put.text)
    #     return result_test_put


