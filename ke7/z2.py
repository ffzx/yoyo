"""
创建一个迭代器
"""


class MyNumber:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        new = self.a
        self.a += 1
        return new


my = MyNumber()
print(my)
myiter = iter(my)
print(next(myiter))
print(next(myiter))
print(myiter.__next__())


