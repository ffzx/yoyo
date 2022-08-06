import pytest


@pytest.fixture(scope="function")
def login_fixture():
    """前置：登录"""
    print("登录，拿到token")
    token = "xxxxx"
    return token


def test_a(login_fixture):
    """测试用例参数，只能传fixture"""
    print(f'拿到token: {login_fixture}')
    print("登录后，用例aaaaaaaaa")