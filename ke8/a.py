import requests

r = requests.get(url="http://49.235.92.12:7005/api/v1/goods?page=1&size=2")
# print(r.status_code)  # 状态码 200
# print(r.headers)
# print(r.text)  # json 格式字符串 (有规律的字符)
# print(type(r.text))  # 原始的接口返回的文本
# json解析器
print(r.json())  # 解析json, 得到python 字典
# print(type(r.json()))  # <class 'dict'>


# 取值
# print(r.headers["Date"])


