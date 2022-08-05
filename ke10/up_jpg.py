import os
"""
运行代码，以当前py文件为  参照物
"""

# 1.当前  运行的py  为参照物
print(__file__)   # D:/202211kecheng/ke10/up_jpg.py  /相对路径  \绝对路径
# 2.跟据不同系统，兼容地址
print(os.path.realpath(__file__))   # 真实的绝对地址
# print(os.path.relpath(__file__))  # 文件名称获取
# 3.公共父目录
print(os.path.dirname(os.path.realpath(__file__)))
print(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print(project_path)

# 4.往下找
print(os.path.join(project_path, 'data', 'yoyo.jpg'))

file_path = os.path.join(project_path, 'data', 'yoyo.jpg')
print(file_path)


import requests

url = "http://49.235.92.12:7005/api/v1/upfile/"

# 多一个files   单独拿出文件图片相关的
"""
3个参数
1.文件、图片名称
2.open读取文件内容， 读取方式rb
3.MIME 类型   jpg格式：image/jpeg
"""
files = {
    "file": ["yoyo.jpg", open(file_path, 'rb'), "image/jpeg"]         # 3个参数
}
# 非文件的参数，放到body,跟之前一样
body = {
    "title": "yoyo.jpg"
}

r = requests.post(url, data=body, files=files)
print(r.status_code)
print(r.text)


