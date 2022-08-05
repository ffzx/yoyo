import requests
from requests import Response, Session


def login(s:Session, base_url, username="test11", password="123456") -> Response:
    url = base_url + "/api/v1/login"
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
    base_url = "http://49.235.92.12:7005"
    s = requests.Session()
    res = login(s, base_url=base_url)
    print(res.text)
    print(s.headers)