"""
断言
"""


def test_x1():
    a = "hello"
    b = "hello world"
    assert a in b


def test_x2():
    a1 = 200
    a2 = [200, 201, 202]
    assert a1 in a2


def test_x3():
    x = "hello"
    y = "world"
    assert x == y, f"{x} 和 {y}不相等"