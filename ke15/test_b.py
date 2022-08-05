"""
为什么工作中很少用这些
"""


def setup():
    print("前置操作")
    token = "xxxxxxxxxxxxxxxxx"   # 局部变量
    return token


def test_a():
    """依赖于token"""
    print("如何拿到token呢？")
    # print(token)    缺陷

