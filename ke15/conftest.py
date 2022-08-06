"""
所有同目录测试文件运行前都会执行conftest.py文件,名称固定不可以更改

共享 fixture, 专门管理所有的fixture


pytest-fixture作用范围：scope便是定义用例域的范围
session > module > class > function

function：默认范围，每一个函数或方法都会调用，不填写时便是它
class：每一个类调用一次
module: 每一个.py文件调用一次，文件中可以有多个function和class
session：多个文件调用一次，可以跨文件，如在.py文件中，每一个.py文件就是module

"""
import pytest


# @pytest.fixture(scope="function")
# def login_fixture():
#     """前置：登录"""
#     print("登录，拿到token")
#     token = "xxxxx"
#     return token

