"""
iter() 和 next()
"""

a = [1, 2, 3, 4]
# for i in a:
#     print(i)
# for j in a:
#     print(j)
b = iter(a)  # 迭代器
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))  # StopIteration


