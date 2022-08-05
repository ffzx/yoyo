"""
fixture 有多个的情况
前置 1
前置 2
前置 3
"""
import pytest


@pytest.fixture()
def login_x():
    print("login--------------")


@pytest.fixture()
def step_1():
    print("step  1111-----------")


@pytest.fixture()
def step_2():
    print("step 222222-----------")


def test_case(login_x, step_1, step_2):
    """测试用例，先登录
    1、step1
    2.step2
    执行case
    """
    print("case 1111111111111111")