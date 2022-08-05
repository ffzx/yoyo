import requests

url = "http://49.235.92.12:7005/api/v1/register"
# 在python里面叫字典  键值对
body = {
    "username": "testxma1",
    "password": "123456",
    "email": "111@qq.com"
}

r = requests.post(url, json=body)
print(r)   # <Response [200]>   response 对象
print(r.status_code)
print(r.headers)
print(r.text)
print(r.json())