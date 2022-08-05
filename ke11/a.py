aa = []
print(type(aa))

bb = ()
print(type(bb))

a1 = ['hello', ]
print(type(a1))
print(a1)

b1 = (11)
print(type(b1))  # 只有一个成员，这个不是元素，当前成员的数据类型

b2 = (12, )
print(b2)
print(type(b2))
# () 运算符
c1 = (1+2)*3
print(c1)

d = tuple([1])
print(d)