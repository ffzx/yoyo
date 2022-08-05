import pytest


def test_1():
    print("11111111")


def test_2():
    print("2222222")


def test_3():
    print("33333333")
    assert 1==2


if __name__ == '__main__':
    print("hello world")  # 走不到
    pytest.main(['-s', 'test_b.py'])
