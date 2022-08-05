"""
post   请求
content-Type   决定 body 传参类型
1. application/json    {"key": "value"}
2. application/x-www-form-urlencoded   key=value&key1=value1
"""
import requests


url = "http://49.235.92.12:7005/api/v1/login"
body = {
    "username": "test",
    "password": "123456"
}
r = requests.post(url, json=body)
print(r.status_code)
print(r.headers)
print(r.text)
# 先看是不是返回json
print(r.json())
print(r.json()['token'])
