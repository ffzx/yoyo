"""
登录用例参数化
"""
from ke15.api.login_api import login
import requests
import pytest
import allure


@allure.feature("登录")
@allure.title("{title}")
@pytest.mark.parametrize("test_input, expected, title", [
    [{"username": "test1", "password": "123456"},  {"code": 0, "msg": "login success!"}, "输入正确账号密码登录成功"],
    [{"username": "test2", "password": ""},  {"code": 3003, "msg": "账号或密码不正确"}, "输入密码为空，登录失败"],
    [{"username": "", "password": "123456"},  {"code": 3003, "msg": "账号或密码不正确"}, "输入账号胃口，登录失败"],
    [{"username": "", "password": ""},  {"code": 3003, "msg": "账号或密码不正确"}, "登录失败"],
])
def test_login_1(test_input, expected, title):
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