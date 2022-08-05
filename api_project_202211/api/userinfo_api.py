import requests
from requests import Session


def add_userinfo(s:Session, base_url, name="test11", sex='F', age=20, mail='123@qq.com'):
    url = base_url + "/api/v1/userinfo"
    body = {
        "name": name,
        "sex": sex,
        "age": age,
        "mail": mail
    }
    r = s.post(url, json=body)
    return r


def get_userinfo(s:Session, base_url):
    url = base_url + "/api/v1/userinfo"
    return s.get(url)
