"""
1.先登录
2.拿到token
3.传到请求头部，替换变量
4.查询商品
"""
import requests

# 1.先登录
url1 = "http://49.235.92.12:7005/api/v1/login"
body = {
   "username": "test11",
   "password": "123456"
}
r1 = requests.post(url1, json=body)
print(r1.status_code)
print(r1.text)
# type 看数据类型
print(type(r1.text))  # <class 'str'>
# python dict 字典取值
print(r1.json())  # json解析器 解析后是 <class 'dict'>
print(type(r1.json()))

# token = r1.json()["token"]  # 如果key不存在 KeyError: 'tokenx'
# print(token)

# 2.拿到token
token2 = r1.json().get('token', '')
print(token2)

# 3.传到请求头部，替换变量

h = {
    "Authorization": f"Token {token2}"
}
print(h)

# 4.查询商品
sp_id = 1
# url2 = f"http://49.235.92.12:7005/api/v2/goods/{sp_id}"
r2 = requests.get(
    url=f"http://49.235.92.12:7005/api/v2/goods/{sp_id}",
    headers=h
)
print(r2.status_code)
print(r2.text)
