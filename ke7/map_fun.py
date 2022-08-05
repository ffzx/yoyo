"""
map 计算成员
"""

x = [1, 2, -3, -9, -11, 20]


# 返回一个新列表，得到绝对值
def func(item):
    """得到绝对值"""
    new_item = abs(item)
    return new_item


res = map(func, x)
print(res)   # map object
print(list(res))
print(list(res))