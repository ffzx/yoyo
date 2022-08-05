"""
fixture autouse=True

如果需要fixture的返回值，不要设置autouse=True
"""
import pytest


@pytest.fixture(scope="function", autouse=True)
def login_x():
    """前置"""
    print("前置-----------------")
    token = 'xxxxxxxxxxxxx'
    return token


def test_1():
    print("case 11111111111111111111")
    print(login_x)  # 对象