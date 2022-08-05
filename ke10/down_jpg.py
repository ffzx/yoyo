"""
图片或文件下载
"""
import requests

url = "http://49.235.92.12:7005/media/up_image/abc.jpg"
r = requests.get(url)
print(r.status_code)
# print(r.text)  # �Au�� �\�I
print(r.content)   # byte类型  b'\xff\xd8\xff\xe0\x00\x

# 保存到本地
with open('下载.jpg', 'wb') as fp:
    fp.write(r.content)

# pdf下载，视频下载，word下载，其它格式文件下载



