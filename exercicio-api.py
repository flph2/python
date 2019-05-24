import requests
# import json
#
# ret = requests.get('https://jsonplaceholder.typicode.com/users')
# for i in ret.json():
#     print(i['username'])
#

data = {
    "title": "AAAAAAA",
    "body": "MSGGG",
    "userid": 123
}

ret = requests.post('https://jsonplaceholder.typicode.com/posts', data)
print(ret.text)
print(ret.status_code)

