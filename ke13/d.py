"""
遇到return结束
"""


def func():
    for i in range(10):
        # i = 0
        if i >= 5:
            return i
        else:
            return "111"  # 遇到return 结束函数


# 结果是什么？
print(func())
