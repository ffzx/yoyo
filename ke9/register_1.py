import requests
"""
用户名用变量，每次注册成功
"""
import time

print(time.time())  # 1656810896.8719816
# 得到前面整数部分
print(int(time.time()))  # 1656810896
# 得到 test_1656810896

# user = "test_{}".format(int(time.time()))
user = "test_" + str(int(time.time()))

url = "http://49.235.92.12:7005/api/v1/register"
# 在python里面叫字典  键值对
body = {
    "username": user,
    "password": "123456",
    "email": "111@qq.com"
}

r = requests.post(url, json=body)
print(r.status_code)
print(r.text)