"""
登录用例参数化
"""
from api.login_api import login
import requests
import pytest
from utils.read_yaml_or_json import read_yml
import os

yaml_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))), 'data', 'data2.yml')
print(yaml_path)
test_date = read_yml(yaml_path)
print(test_date)


@pytest.mark.parametrize("test_input, expected", test_date)
def test_login_1(test_input, expected, base_url):
    """
    登录成功场景-输入正确账号，正确密码，登录成功
    :return:
    """
    s = requests.Session()
    r = login(s, base_url, test_input["username"], test_input["password"])
    print(r.text)
    # 断言
    assert r.json()["code"] == expected["code"]
    assert r.json()["msg"] == expected["msg"]