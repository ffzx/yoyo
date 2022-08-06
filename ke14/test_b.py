import pytest

"""
pytest框架和python有不同
遇到test开头的自动识别执行，
不会去执行if __name__ == '__main__':，也没有这样用的
"""


def test_1():
    print("11111111")


def test_2():
    print("2222222")


def test_3():
    print("33333333")
    assert 1 == 2


if __name__ == '__main__':
    print("hello world")  # 走不到
    pytest.main(['-s', 'test_b.py'])
