"""
range(start, stop[, step])
Start 起始位置 0
Stop  终点 位置
Step 步长 1
"""

print(list(range(10)))
print(list(range(0, 11)))
print(list(range(0, 11, 2)))

print(list(range(9, 0, -1)))


for i in range(10):
    print(i)
