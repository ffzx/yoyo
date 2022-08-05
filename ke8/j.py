"""乱码解决"""

import requests

url = 'http://www.baidu.com'
r = requests.get(url)
print(r.text)     # ¾åº¦ä¸ä¸ï¼ä½ å°±ç¥é 乱码
# charset=utf-8
print(r.encoding)   # ISO-8859-1

# 改变encoding 属性
r.encoding = "utf-8"   # 首先知道编码才能解码
print(r.text)