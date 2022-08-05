"""
[1, 2, 3, 4, 5, 6, 7]
找出大于3 的成员
"""
a = [1, 2, 3, 4, 5, 6, 7]

# 做作业，笔试的时候，这样写（尽量不要内置函数）
# aa = []
# for i in a:
#     if i > 3:
#         aa.append(i)
# print(aa)

# 自己写代码的时候 filter() 过滤操作
# 筛选满足条件的成员


def fun(item):
    """判断条件"""
    return item > 3


res = filter(fun, a)
print(res)   # filter object 可迭代对象
print(list(res))

