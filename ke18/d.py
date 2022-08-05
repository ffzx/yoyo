"""
类：属性(类属性 和 实例属性) 和 方法:self 实例方法，静态方法，类方法，私有方法，魔法方法（构造方法.....)

1.实例对象，可以调用类属性和实例实例（self)
2.类对象，只能调用类属性，不能调用实例属性

cls类方法@classmethod   实例方法（self)   静态方法（实际上是函数）

cls 类方法不能调用实例方法
self 实例方法 可以调用类方法
"""

class People(object):

    height = 180  # 类属性
    weight = 40

    def __init__(self, colour):
        """构造函数"""
        age = 0   # 局部属性
        self.colour = colour   # 实例属性

    @classmethod
    def shuohua(cls):
        print("说话")


    def chifan(self):
        print(self.colour)
        print(self.height)
        print(self.shuohua())

    @staticmethod
    def hanshu():
        print("普通函数")

    def __repr__(self):
        return f"<People object  {self.colour}>"


if __name__ == '__main__':
    print(People)
    print(People.height)
    print(People.weight)
    print(People.shuohua())
    print(People.hanshu())
    p = People(colour='黄皮肤')
    print(p)
    p2 = People(colour='黑皮肤')
    print(p2)
    p.chifan()
    print(p.height)
    print(p.colour)
    print(p.shuohua())
    print(p.hanshu())