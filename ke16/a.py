"""
函数作为另外一个函数的参数
"""


def func():
    return "hello"


def funx():
    return "aaaa"


def demo(f):
    print(f)
    print("执行f")
    res = f()  # 执行
    return res + "world"


if __name__ == '__main__':
    print(demo(func))
    print(demo(funx))



