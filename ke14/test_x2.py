"""
测试用例的误区
1.执行的误区
if __name__ == '__main__':
    test_x1()

2.测试用例的参数  fixture 'a' not found
参数：fixture 夹具 (脚手架)
脚手架：
1.用例的前置setup: 数据准备工作
2.用例的后置teardown：还原数据，清理数据
"""


def setup_module():
    print("整个py文件只执行一次")


def setup():
    print("前置操作：数据准备")


def teardown():
    print("后置操作：数据清理")


def test_x1():
    print("hello world")


def test_x2():
    print("xxx")


def teardown_module():
    print("整个py模块用例完成后只执行一次")

