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

    # # Get current User
    # current_user_endpoint = '/auth/me'
    # # wrong accessToken
    # get_wrong_user = get_current_user(root_url + current_user_endpoint, "123")
    # print('***get_wrong_user', get_wrong_user)
    #
    # # correct accessToken
    # get_user = get_current_user(root_url + current_user_endpoint, user.accessToken)
    # print('***get_user', get_user)

    refresh_auth_endpoint = '/auth/refresh'
    refresh_auth_response = get_refresh_auth_token(root_url + refresh_auth_endpoint, user.refreshToken, 30)

    print(refresh_auth_response)
    newAccessToken, newRefreshToken = (
        refresh_auth_response['accessToken'], refresh_auth_response['refreshToken']
    )

    print("  new auth token: ***  ")
    print(newAccessToken, "\n", newRefreshToken)
    print(newRefreshToken == user.refreshToken)
