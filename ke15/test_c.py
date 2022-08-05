"""
fixture  作用：
1.可以拿到前置参数
2.可以自定义前置和后置名称
"""
import pytest


# @pytest.fixture(scope="function")
# def login_fixture():
#     """前置：登录"""
#     print("登录，拿到token")
#     token = "xxxxx"
#     return token


def test_1(login_fixture):
    """测试用例参数，只能传fixture"""
    print(f'拿到token: {login_fixture}')
    print("登录后，用例1")


def test_2():
    print("登录后，用例2")


def test_3():
    print("登录后，用例3")