"""乱码解决"""
import warnings
warnings.filterwarnings('ignore')  # 忽略警告
import requests

url = 'https://www.baidu.com'  # https 打开了fiddler SSLError
r = requests.get(url, verify=False)
print(r.text)     # ¾åº¦ä¸ä¸ï¼ä½ å°±ç¥é 乱码
# charset=utf-8
print(r.encoding)   # ISO-8859-1 解码
print(r.apparent_encoding)   # 从返回的页面获取真实的编码  utf-8

print(r.content.decode(r.apparent_encoding))