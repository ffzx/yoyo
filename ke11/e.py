a = {
    "name": "yoyo",
    "mail": "123@qq.com",
    "age": "22",
    "tel": "12345678901"
}

# 可迭代对象，就可以for 遍历
# for i in a:
#     print(i)


for key, value in a.items():
    print(key, value)