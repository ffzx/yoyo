import requests

g_id = 181
url = f"http://49.235.92.12:7005/api/v1/goods/{g_id}"
print(url)

r = requests.get(url)
# 返回的是response 对象
print(r)     # <Response [200]> object
print(r.status_code)
print(r.content)        # byte   解决返回内容乱码的时候会用到
print(r.url)  # http://49.235.92.12:7005/api/v1/goods/181
print(r.encoding)  # 默认的编码 utf-8
print(r.cookies)  # 单独拿出来 <RequestsCookieJar[]>
print(r.apparent_encoding)

