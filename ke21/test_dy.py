"""
用例动态加描述
"""
import allure


def test_c1():
    allure.dynamic.feature("登录功能")
    allure.dynamic.title("标题")
    with allure.step("步骤1"):
        print("111111111111111")
