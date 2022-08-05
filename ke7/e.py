"""
else 是for正常循环完才执行，有 break执行的时候  不执行=
"""
a = [1, 2, 3, 4, 5]
for i in a:
    print(i)
    if i > 4:
        break
else:
    print("正常执行完成")