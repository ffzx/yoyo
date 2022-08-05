"""
转义字符 \
"""

x = "hello world\\"
print(x)

y = "hello \" world"
print(y)

z ="hello \n world"
print(z)

path = "D:\hello\world"
print(path)

path1 = "D:\\new\\row"
print(path1)

import keyword
print(keyword.kwlist)

# row 不转义
path2 = r"D:\new\row"
print(path2)



