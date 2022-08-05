"""
添加商品
"""
import requests
import time


code = "sp_"+str(int(time.time()))
url = "http://49.235.92.12:7005/api/v1/goods"
body = {
  "goodsname": "学习商品名称1",
  "goodscode": code
}

r = requests.post(url, json=body)
print(r.status_code)
print(r.text)