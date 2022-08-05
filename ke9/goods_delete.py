"""
删除商品 id
前提条件，数据库存在对应商品id
"""
import requests

sp_id = 164   # 存在的
url = f"http://49.235.92.12:7005/api/v1/goods/{sp_id}"
r = requests.delete(url)
print(r.status_code)
print(r.text)

