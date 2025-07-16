import requests

# Making a GET request
# r = requests.get('https://jsonplaceholder.typicode.com/users/1')
#
# print(r)
#
# data = r.json()
# print("data: ", data)
# user = dict(data)
#
# for key, value in user.items():
#     print(key, value, sep=": ");

r = requests.get('https://jsonplaceholder.typicode.com/users')

print(r)

data = r.json()
# print("data: ", data)
users = []

for item in data:
    users.append(dict(item))

for user in users:
    print(user)