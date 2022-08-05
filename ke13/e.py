"""
函数有参数的情况
"""


def func(x, y):
    """
    函数功能
    :param x: str
    :param y: str
    :return: str
    """
    print(f"x: {x}")
    print(f"y: {y}")
    return x+y

s = func(y="hello", x="world")
print(s)