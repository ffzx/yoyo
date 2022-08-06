"""
map 计算成员


Python map 函数是一个允许你使用另一个函数转换整个可迭代对象的函数。
Python map 函数不是遍历字符串列表的每个项目，而是将整个字符串列表转换为数字列表。你节省了内存，并且代码运行得更快。

如果用for 循环的话，需要遍历一遍，再添加进空列表，显然map函数更优雅
"""

x = [1, 2, -3, -9, -11, 20]
#
# result = []
#
# for string in x:
#     result.append(abs(string))
# print(result)

# new_item = map(abs, x)  # map object
# print(list(new_item))




# 返回一个新列表，得到绝对值
# def func(item):
#     """得到绝对值"""
#     new_item = abs(item)
#     return new_item
#
#
# res = map(func, x)
# print(res)   # map object
# print(list(res))
