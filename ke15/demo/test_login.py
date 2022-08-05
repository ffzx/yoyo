from ke15.api.login_api import login
import requests


def test_login_1():
    """
    登录成功场景-输入正确账号，正确密码，登录成功
    :return:
    """
    s = requests.Session()
    r = login(s, "test11", "123456")
    print(r.text)
    # 断言
    assert r.json()["code"] == 0
    assert r.json()["msg"] == "login success!"
    assert len(r.json()["token"]) == 40


def test_login_2():
    """
    登录失败场景-输入正确账号，错误密码，登录失败
    :return:
    """
    s = requests.Session()
    r = login(s, "test12", "123456xxx")
    print(r.text)
    assert r.json()["code"] == 3003
    assert r.json()["msg"] == "账号或密码不正确"
    assert len(r.json()["token"]) == 0


def test_login_3():
    """
    登录失败场景-输入正确账号，错误为空，登录失败
    :return:
    """
    s = requests.Session()
    r = login(s, "test12", "")
    print(r.text)
    assert r.json()["code"] == 3003
    assert r.json()["msg"] == "账号或密码不正确"
    assert len(r.json()["token"]) == 0


def test_login_4():
    """
    登录失败场景-输入正确账号，错误为空，登录失败
    :return:
    """
    s = requests.Session()
    r = login(s, "", "")
    print(r.text)
    assert r.json()["code"] == 3003
    assert r.json()["msg"] == "账号或密码不正确"
    assert len(r.json()["token"]) == 0
