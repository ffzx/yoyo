"""
关键字参数
"""

def func(x, y=0):
    """关键字参数"""
    print(f"x: {x}")
    print(f"y: {y}")
    return x+y

func(10, y=20)