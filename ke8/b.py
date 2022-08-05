"""
get 请求参数处理
url="http://49.235.92.12:7005/api/v1/goods?page=1&size=2"
"""
import requests


url = "http://49.235.92.12:7005/api/v1/goods"
# page=1&size=2
params = {
    "page": "1",
    "size": "2"
}
r = requests.get(url=url, params=params)
print(r.status_code)
print(r.headers)
print(r.text)