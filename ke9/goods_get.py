"""
查询单个商品
id 不能设置为变量，python里面的内置函数
a = "hello"
print(id(a))   # id是指变量存储的内存地址
"""
import requests

sp_id = 1   # 可变的地方用变量，单独拿出来
url = f"http://49.235.92.12:7005/api/v1/goods/{sp_id}"
r = requests.get(url)
print(r.status_code)
print(r.text)

