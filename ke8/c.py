"""
get 请求url 地址路径参数
/api/v1/goods/{id}    {id} 接口文档里面代表变量
"""
import requests


# id 是python的内置函数
g_id = 181
url = f"http://49.235.92.12:7005/api/v1/goods/{g_id}"
print(url)

r = requests.get(url)
print(r.status_code)
print(r.headers)
print(r.text)

