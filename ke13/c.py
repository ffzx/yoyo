"""
函数没有return
return 和 print的区别
"""


def demo():
    print("hello world")   # 输出不是函数的结果
    print("2222222222")
    return

res = demo()
print(res)   # None


