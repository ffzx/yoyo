x = "111"




from collections import Iterable
r = isinstance(x, Iterable)
print(r)

if isinstance(x, Iterable):
    # 判断x是不是可迭代对象  iterable
    for i in x:
        print(i)







