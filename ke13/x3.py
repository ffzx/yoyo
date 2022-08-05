"""
匿名函数 lambda
是一种特殊函数(没有函数名称)

所有的匿名函数都可以转成标准函数
"""


def func(x):
    return x*x


a = func(2)
print(a)

f = lambda x: x*x
print(f(3))


def key1(x):
    return abs(x)

key = lambda x: abs(x)