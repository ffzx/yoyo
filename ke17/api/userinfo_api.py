import requests
from requests import Session


def add_userinfo(s:Session, name="test11", sex='F', age=20, mail='123@qq.com'):
    url = "http://49.235.92.12:7005/api/v1/userinfo"
    body = {
        "name": name,
        "sex": sex,
        "age": age,
        "mail": mail
    }
    r = s.post(url, json=body)
    return r


def get_userinfo(s:Session):
    url = "http://49.235.92.12:7005/api/v1/userinfo"
    return s.get(url)
