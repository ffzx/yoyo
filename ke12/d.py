"""
模拟浏览器web登录
1.get 请求，正常打开登录页
2.输入参数之后
3.发post 登录
"""
import requests
import re


s = requests.Session()


url = "http://49.235.92.12:7005/xadmin/"
# 发get 请求：1.拿到服务器给的cookie， 2.拿到页面上的隐藏参数
r = s.get(url)
# print(r.text)
csrf_token = re.findall("name='csrfmiddlewaretoken' value='(.+?)'", r.text)
print(csrf_token[0])

body = {
    "csrfmiddlewaretoken": csrf_token[0],
    "username": "admin",
    "password": "yoyo123456",
    "this_is_the_login_form": "1",
    "next": "/xadmin/"
}
r2 = s.post(url, data=body)
print(r2.text)


