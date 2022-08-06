import requests
from requests import Response, Session


"""
先写api,传缺省参数
写testcase的时候，调佣api，传其他需要测试的参数
"""
def login(s: Session, username="test11", password="123456") -> Response:
    url = "http://49.235.92.12:7005/api/v1/login"
    body = {
        "username": username,
        "password": password
    }
    r = s.post(url, json=body)
    token = r.json()["token"]
    h = {
        "Authorization": f"Token {token}"
    }
    s.headers.update(h)
    return r


if __name__ == '__main__':
    s = requests.Session()
    res = login(s)
    print(res.text)
    print(s.headers)
