"""
内置函数的使用
"""
print(dir(__builtins__))

a = "hello"

print(id(a))
print(type(a))

d = [1, 2, 3, 4]  # list
print(len(d))   # 函数
print(d.__len__())  # list本身的方法调用

# sorted 排序
print(sorted(d))
print(d.sort())   # list 对象才有的方法



