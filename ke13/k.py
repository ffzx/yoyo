"""
kwargs 接收多余的关键字参数
** 语法  字典分解成 x=1, y=2
a = {
    "x": 1,
    "y": 2
}
b = {
    "z": 12
}
b.update(x=1, y=2)
print(b)
"""


def func(x, y=0, z=0, *args, **kwargs):
    print(f"x: {x}")
    print(f"y: {y}")
    print(f"z: {z}")
    print(f"args: {args}")
    print(kwargs)


func(4, 5, 6, 7, 9, h=4)






