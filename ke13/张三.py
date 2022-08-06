"""
标准写法
声明 x传什么类型
声明返回的结果是什么对象

 -> 声明类型，方便编辑器能识别 返回的结果继续调用方法

"""
from typing import List


def func(x:str, y:str) -> List:
    """

    :param x: str
    :param y: str
    :return:
    """
    return [x, y]


if __name__ == '__main__':
    # 仅仅只在当前py 文件执行
    r = func("hello", "world")  # 自测的内容
    print(r)