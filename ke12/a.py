"""
为什么会要Session
能帮助我们解决哪些问题
如何去使用
"""
import requests

s = requests.Session()   # Session() 实例 (虚拟浏览器概念)
url = "http://49.235.92.12:7005/api/v1/login"
body = {
    "username": "test11",
    "password": "123456"
}
r1 = s.post(url, json=body)
print(r1.text)
print(r1.json())
token = r1.json().get("token", '')
print(token)

# 希望，后面的请求都带上token
s.headers.update({"Authorization": f"Token {token}"})
print(s.headers)


# 后面所有的s发出去的请求。都会带上'Authorization': 'Token
url2 = "http://49.235.92.12:7005/api/v1/userinfo"
r2 = s.get(url2)
print(r2.text)

# 更新 post
body3 = {
    "name": "test11",
    "sex": "M",
    "age": 20,
    "mail": "283340479@qq.com"
}
r3 = s.post(url2, json=body3)
print(r3.text)






