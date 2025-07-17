from httpRequest.dummy_http_utils import *
import requests


if __name__ == '__main__':
    #  Login
    root_url = 'https://dummyjson.com'
    auth_endpoint = './auth/login'

    payload = {
        'username': 'emilys',
        'password': 'emilyspass',
        'expiresInMins': 30  # tùy chọn, mặc định là 60
    }

    headers = {
        'Content-Type': 'application/json'
    }

    user = login(root_url + auth_endpoint, payload, headers)
    # print(user)
    # print(user.accessToken)

    # Get current User
    current_user_endpoint = '/auth/me'
    # wrong accessToken
    get_wrong_user = get_current_user(root_url + current_user_endpoint, "123")


    get_user = get_current_user(root_url + current_user_endpoint, user.accessToken)
    print('***get_user', get_user)
