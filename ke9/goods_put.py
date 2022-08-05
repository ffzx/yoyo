"""
修改商品
前提：必须商品存在，才能修改
"""
import requests


sp_id = 1   # 存在的
url = f"http://49.235.92.12:7005/api/v1/goods/{sp_id}"
body = {
    "goodsname": "修改后的商品名称",
    "goodscode": "sp_test1"
}
r = requests.put(url, json=body)
print(r.status_code)
print(r.text)
