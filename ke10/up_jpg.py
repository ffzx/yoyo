import os
import sys

"""
运行代码，以当前py文件为  参照物
"""

# 1.当前  运行的py  为参照物
# print(sys.path)

# print(f"__file__是:{__file__}")
"""
用命令行执行时候
如果当前文件包含在sys.path里面，那么，__file__返回一个相对路径！
如果当前文件不包含在sys.path里面，那么__file__返回一个绝对路径！

pycharm自动把当前项目文件加进sys.path了？
"""
# 2.跟据不同系统，兼容地址
print(os.path.realpath(__file__))   # realpath  当前文件真实的绝对地址
print(os.path.relpath(__file__))  # relpath  当前文件相对路径|当前文件名称获取
# # 3.父目录
print(os.path.dirname(os.path.realpath(__file__)))
print(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# print(project_path)
#
# # 4.往下找
print(os.path.join(project_path, 'data', 'yoyo.jpg'))

file_path = os.path.join(project_path, 'data', 'yoyo.jpg')
print(file_path)


import requests

# url = "http://49.235.92.12:7005/api/v1/upfile/"

# 多一个files   单独拿出文件图片相关的
"""
3个参数
1.文件、图片名称
2.open读取文件内容， 读取方式rb
3.MIME 类型   jpg格式：image/jpeg
"""
# files = {
#     "file": ["yoyo.jpg", open(file_path, 'rb'), "image/jpeg"]         # 3个参数
# }
# # 非文件的参数，放到body,跟之前一样
# body = {
#     "title": "yoyo.jpg"
# }
#
# r = requests.post(url, data=body, files=files)
# print(r.status_code)
# print(r.text)


