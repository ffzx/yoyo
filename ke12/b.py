import requests

s = requests.Session()
print(s.headers)     # 默认自带的
print(type(s.headers))
s.headers.update({"Authorization": "Token 63914bfa94c81c09c4c93354519924e3d32cb5bc"})
print(s.headers)


r1 = s.get("http://49.235.92.12:7005/api/test/demo")
print(r1)
r2 = s.get("http://49.235.92.12:7005/api/test/demo")
print(r2)
