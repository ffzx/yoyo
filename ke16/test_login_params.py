"""
登录用例参数化
"""
from ke15.api.login_api import login
import requests
import pytest


@pytest.mark.parametrize("test_input, expected", [
    [{"username": "test1", "password": "123456"},  {"code": 0, "msg": "login success!"}],
    [{"username": "test2", "password": ""},  {"code": 3003, "msg": "账号或密码不正确"}],
    [{"username": "", "password": "123456"},  {"code": 3003, "msg": "账号或密码不正确"}],
    [{"username": "", "password": ""},  {"code": 3003, "msg": "账号或密码不正确"}],
])
def test_login_1(test_input, expected):
    """
    登录成功场景-输入正确账号，正确密码，登录成功
    :return:
    """
    s = requests.Session()
    r = login(s, test_input["username"], test_input["password"])
    print(r.text)
    # 断言
    assert r.json()["code"] == expected["code"]
    assert r.json()["msg"] == expected["msg"]