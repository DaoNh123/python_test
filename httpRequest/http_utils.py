import inspect
import requests

def get_all(url):
    res = requests.get(url)

    list_dict = [item for item in res.json()]
    return list_dict

def get_one(url):
    res = requests.get(url)

    print(type(res.json()), " : ", res.json())
    return res.json()

def post_one(url, data):
    res = requests.post(url, data=data)

    print(inspect.currentframe().f_code.co_name , res.status_code, " : ", res.json())
    return res.json()

def put_one(url, data):
    res = requests.put(url, data=data)

    print(inspect.currentframe().f_code.co_name , res.status_code, " : ", res.json())
    return res.json()

def patch_one(url, data):
    res = requests.patch(url, data=data)

    print(inspect.currentframe().f_code.co_name , res.status_code, " : ", res.json())
    return res.json()

def delete_one(url):
    res = requests.delete(url)

    print(inspect.currentframe().f_code.co_name , res.status_code, " : ", res.json())
    return res.json()