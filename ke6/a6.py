"""
列表的值是可变的
"""
x = "hello"

a = ["hello", "world"]
print(a)
print(id(a))

a[0] = 123
print(a)
print(id(a))