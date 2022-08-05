"""
万能传参
用在装饰器里面
或者，封装其它方法的时候
"""


def func(*args, **kwargs):
    """万能的参数"""
    print(args)
    print(kwargs)


func(2, 3, x=1, y=3)


