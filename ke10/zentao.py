"""
网站的登录
仅仅是这个网站，刚好可以用原始密码登录
"""
import requests

url = "http://49.235.92.12:8080/zentao/user-login.html"
body = {
    "account": "admin",
    "password": "YOYO123456",
    "passwordStrength": "1",
    "referer": "/zentao/",
    "verifyRand": "1275225899",
    "keepLogin": "0"
}

"""
ajax 异步，局部更新网页数据
"""
h = {
    "X-Requested-With": "XMLHttpRequest"
}

r = requests.post(url, data=body, headers=h)
print(r.content)
print(r.text)
