import inspect
import requests
from user import *

from httpRequest.user import User


def login(url, payload, headers):
    response = requests.post(url, json=payload, headers=headers)

    # In ra JSON response
    print(response.status_code)
    print(response.json())
    print(" *** ")
    return User(**(response.json()))

def get_current_user(url, accessToken):
    headers = {'Authorization': f'Bearer {accessToken}'}

    response = requests.get(url, headers=headers)
    print(response.status_code)
    print(response.json())

    return dict(response.json())
