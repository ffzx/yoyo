"""
不知道参数有几个
*args 作用：接收多余的参数
参数的顺序
x
z=0,
*args
"""


def sum_(x, y, z=0, *args):
    """与内置函数做区分"""
    print(f"x: {x}")
    print(f"y: {y}")
    print(f"z: {z}")
    print(args)  # tuple
    return sum(args)


y = (2, 3, 4, 5)   # []  ()
print(sum_(*y))

