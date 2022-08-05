"""
Iterator 迭代器
"""
from collections import Iterable, Iterator

a = "hello world"  # 可迭代对象  不是迭代器
print(isinstance(a, Iterable))  # True
print(isinstance(a, Iterator))  # False

# 转成迭代器 iter() 内置的函数
b = iter(a)  # 迭代器
print(b)  # iterator object 迭代器 对象
print(b.__next__())
print(next(b))
print(next(b))  # 只能next取值

# for 用于 操作可迭代对象( 基础str list,, 迭代器)
# for j in b:
#     print(j)

for k in range(5):
    xxx = next(b)

