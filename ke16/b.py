import time

"""
装饰器
写个公共的方法，作用是针对函数的
把函数对象，当成参数
"""


def demo(f):
    """装饰器---标准的写法"""
    def inner():
        t1 = time.time()
        res = f()  # 执行
        t2 = time.time()
        print(f"运行时间：{t2 - t1}")
        return res
    return inner


@demo
def fun_a():
    """领导说先sleep 2秒"""
    time.sleep(2)
    print("aaaaaa")


@demo
def fun_b():
    """领导说先sleep 1.5秒"""
    time.sleep(1.5)
    print("bbbbb")


if __name__ == '__main__':
    # demo(fun_a)()
    # demo(fun_b)()
    fun_a()
    fun_b()