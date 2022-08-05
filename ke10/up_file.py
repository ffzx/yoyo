"""
multipart/form-data;
文件上传接口
"""
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
    "file": ["abc.jpg", open('abc.jpg', 'rb'), "image/jpeg"]         # 3个参数
}
# 非文件的参数，放到body,跟之前一样
body = {
    "title": "非文件相关的，文件标题"
}

r = requests.post(url, data=body, files=files)
print(r.status_code)
print(r.text)