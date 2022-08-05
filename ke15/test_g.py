"""
如果fixture 依赖于 另外一个fixture（可以直接传）

1.登录fixture
2.添加商品 （ 需要依赖登录）
3.查询商品

# 1.test用例参数，可以传fixture
2.fixture的参数，也可以传fixture
"""
import pytest


@pytest.fixture(scope="function")
def login_fixture():
    print("login 111111111")
    token = "token xxxxxxxxxx"
    return token


@pytest.fixture(scope="function")
def add_goods(login_fixture):
    print(f"需要token：{login_fixture}")
    return "sp id--------"


def test_case(add_goods):
    print("case ........")
    print(add_goods)
    # 查询商品
