"""
封装其它函数
"""
import requests

requests.get()


def func(x, y=0, z=0, *args, **kwargs):
    print(f"x: {x}")
    print(f"y: {y}")
    print(f"z: {z}")
    print(f"args: {args}")
    print(kwargs)


def new(*args, **kwargs):
    return func(*args, **kwargs)

new(1, 2, 3, 4, 5)