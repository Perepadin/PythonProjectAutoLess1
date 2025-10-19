import requests

"""Список HTTP методов"""
class Http_method:
    headers = {'Contetn-Tyep': 'application/json'}
    cookie = ''

    @staticmethod
    def custom_get_method(url):
        result = requests.get(url, headers=Http_method.headers)
        return result

    def custom_post_method(url,body):
        result = requests.post(url, json=body, headers=Http_method.headers)
        return result

    def custom_put_method(url,body):
        result = requests.put(url, json=body, headers=Http_method.headers)
        return result

    def custom_delete_method(url,body):
        result = requests.delete(url, json=body, headers=Http_method.headers, cookie=Http_method.cookie)
        return result