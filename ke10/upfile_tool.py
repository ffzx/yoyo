"""
requests-toolbelt
"""
from requests_toolbelt import MultipartEncoder
import requests


url = "http://49.235.92.12:7005/api/v1/upfile/"

m = MultipartEncoder(
    fields={
        "title": "yoyo.jpg",
        "file": ["yoyo.jpg", open('abc.jpg', 'rb'), "image/jpeg"]         # 3个参数
    }
)

r = requests.post(url, data=m, headers={'Content-Type': m.content_type})
print(r.status_code)
print(r.text)

