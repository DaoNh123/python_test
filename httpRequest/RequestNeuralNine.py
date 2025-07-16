# import requests
#
# params = {
#     "name" : "Mike",
#     "age": 25
# }
# # Using https://httpbin.org/
# response = requests.get('https://httpbin.org/get?name=Mike', params=params)
# print(response.url)  # https://httpbin.org/get?name=Mike&name=Mike&age=25
#
# print(response.status_code)
# res_json = response.json()
# del res_json['origin']  # remove local IP
#
# print(res_json)
#
# personalData = dict(res_json['args'])
# print(personalData)

# import requests
#
# # Using https://httpbin.org/
# response = requests.get('https://httpbin.org/get')
#
# res_json = response.json()
# del res_json['origin']
# print(res_json)
#
# del res_json['origin']  # remove local IP
# print(res_json['args'])
#
# for item in res_json['args']:
#     print(item)

# # POST
# import requests
#
# payload = {
#     "name" : "Mike",
#     "age": 25
# }
# # Using https://httpbin.org/
# response = requests.post('https://httpbin.org/post', data=payload)
#
# res_json = response.json()
# del res_json['origin']
# print(res_json)


# #Handle Status Code
# import requests
#
# # Using https://httpbin.org/
# response = requests.get('https://httpbin.org/status/500')
#
# if response.status_code == requests.codes.not_found:
#     print("NOT FOUND")
# else:
#     print(response.status_code)

# import requests
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0",
#     "Accept": "image/png"
# }
#
# # Using https://httpbin.org/
# response = requests.get('https://httpbin.org/image', headers=headers)
#
# with open("myimage.png", "wb") as f:
#     f.write(response.content)

# import requests
#
# # Using https://httpbin.org/
# response = requests.get('https://httpbin.org/delay/2', timeout=(5, 10))
#
# res_json = response.json()
# del res_json['origin']
# print(res_json)

# Proxies
import requests
proxies = {
    "http" : "139.99.237.62:80",
    "https" : "139.99.237.62:80"
}
# Using https://httpbin.org/
response = requests.get('https://httpbin.org/get', proxies=proxies)

print(response.text)
