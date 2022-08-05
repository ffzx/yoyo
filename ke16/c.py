"""
最基础的参数化案例
参数化的场景：
测试步骤也一样，测试输入和输出不一样
"""
import pytest


@pytest.mark.parametrize("test_input, expected", [
    ["1+2", 3],
    ["2+3", 5],
    ["3+4", 7],
])
def test_eval(test_input, expected):
    """eval 字符串当代码执行"""
    print(f"test_input 输入的内容：{test_input}")
    print(f"expected 期望的结果：{expected}")
    assert eval(test_input) == expected



@pytest.mark.parametrize("test_input, expected", [
    [{"username": "test1", "password": "123456"}, {"code": 0, "msg": "success"}],
    [{"username": "test2", "password": ""}, {"code": 3003, "msg": "账号或密码不正确"}],
    [{"username": "", "password": "123456"}, {"code": 3003, "msg": "账号或密码不正确"}],
    [{"username": "", "password": ""}, {"code": 3003, "msg": "账号或密码不正确"}],
])
def test_login_demo(test_input, expected):
    """eval 字符串当代码执行"""
    print(f"test_input 输入的内容：{test_input}")
    print(f"expected 期望的结果：{expected}")


