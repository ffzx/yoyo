"""
函数
1.函数能干什么
2.函数名称
3.函数有没有参数
4.有没有返回值
"""


def add():
    """
    函数描述：实现2个数相加
    :return: 返回2个数相加的结果
    """
    x = "hello"
    y = "world"
    s = x + y
    return s


print(add)   # 在内存里面的一个地址 函数对象
print(id(add))
print(add())   # 圆括号是一个语法，触发函数

# 2个概念，1.函数对象   2.执行函数
# 函数本身也可以作为一个参数 （装饰器）
