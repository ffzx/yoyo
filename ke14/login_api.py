import requests
from requests import Response


def login(username="test11", password="123456") -> Response:
    url = "http://49.235.92.12:7005/api/v1/login"
    body = {
        "username": username,
        "password": password
    }
    r = requests.post(url, json=body)
    return r


if __name__ == '__main__':
    r = login()
    print(r.text)
