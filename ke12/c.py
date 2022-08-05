"""
Session() 会话实例，可以自动关联cookies，不需要取出来
"""
import requests

s = requests.Session()
print(s)
print(s.headers)
print(s.cookies)     # 代码里面 cookies 单独拿出来了 <RequestsCookieJar[]>
print(dict(s.cookies))  # {} 默认为空

# 自动获取cookie (cookie是服务器给过来的你才有)
# 拿到服务器给的，需要访问哪个地址，服务器会给（一般访问首页，模拟人工操作)
url = "http://49.235.92.12:7005/api/v1/login"
body = {
    "username": "test11",
    "password": "123456"
}
print(s.cookies)
r1 = s.post(url, json=body)
print(s.cookies)
print(s.headers)

# 验证 cookies 通过session会话，自动关联
s.get("http://49.235.92.12:7005/api/test/demo")

# print(r1.headers)
# print(r1.headers.get('Set-Cookie'))   # sessionid=f2pbw9uyt90c0nk6tdou39hjk38g0a07;
# print(r1.cookies)
# print(dict(r1.cookies))    # 不建议去取出 cookies




