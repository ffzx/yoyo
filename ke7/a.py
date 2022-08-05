books = ["python 入门", "JavaScript", "SQL数据库"]
# print(books[0])  # 下标从0开始
# print(books[1])
# print(books[2])
# print(books[-1])
# print(books[-2])
# # 切片
# print(books[:])
# print(books[3])   # IndexError: list index out of range

# 循环了3次 循环的是 item
for i in ["python 入门", "JavaScript", "SQL数据库"]:
    print(i)

# 循环 range() 函数
x = range(10)    # [0, 1, ,,,,,9]
print(x)         # range(0, 10)  object
print(list(x))   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for j in range(10):
    print(j)
print(len(books))     # 3
for k in range(len(books)):  # 循环的是列表的下标
    print(k)
    print(books[k])
