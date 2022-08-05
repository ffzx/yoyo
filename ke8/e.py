"""
r.json() 不是随便用的
"""
import requests

url = "http://www.baidu.com"
r = requests.get(url)
print(r.status_code)
print(r.text)
#用的时候要注意，不能随便用
# print(r.json()) # 用的时候要注意，不能随便用

# {"code":0,"msg":"success!"}