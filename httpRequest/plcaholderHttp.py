import requests
from http_utils import *

if __name__ == '__main__':
    #  getAll
    root_url = "https://jsonplaceholder.typicode.com"
    get_all_endpoint = '/posts'
    posts = get_all(root_url + get_all_endpoint)
    # for post in posts:
    #     print(post)

    #   getOne
    get_one_endpoint = '/posts/1'
    post = get_one(root_url + get_one_endpoint)

    #postOne
    post_one_endpoint = '/posts'
    data = {
        "userId": 1,
        "id": 1,
        "title": "sunt aut facere",
        "body": "body1"
    }
    post_one(root_url + post_one_endpoint, data)

    #putOne
    put_one_endpoint = '/posts/1'
    data = {
        "body": "body1"
    }
    put_one(root_url + put_one_endpoint, data)

    #patchOne
    patch_one_endpoint = '/posts/1'
    data = {
        "body": "body1"
    }
    patch_one(root_url + patch_one_endpoint, data)

    #deleteOne
    delete_one_endpoint = '/posts/1'
    data = {
        "body": "body1"
    }
    delete_one(root_url + delete_one_endpoint)
