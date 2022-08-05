import pytest
"""
测试用例只能传2种数据
1.fixture
2.参数化parametrize的变量 test_input, expected
"""


@pytest.fixture(scope="session")
def demo_fixture():
    print("前置操作！！！！！！")


@pytest.mark.parametrize("test_input, expected", [
    [{"username": "test1", "password": "123456"}, {"code": 0, "msg": "success"}],
    [{"username": "test2", "password": ""}, {"code": 3003, "msg": "账号或密码不正确"}],
    [{"username": "", "password": "123456"}, {"code": 3003, "msg": "账号或密码不正确"}],
    [{"username": "", "password": ""}, {"code": 3003, "msg": "账号或密码不正确"}],
])
def test_login_demo(test_input, expected, demo_fixture):
    """eval 字符串当代码执行"""
    print(f"test_input 输入的内容：{test_input}")
    print(f"expected 期望的结果：{expected}")
