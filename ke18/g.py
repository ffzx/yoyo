class Father(object):

    def __init__(self):
        self.age = 40
        self.name = "father"
        self.address = '上海市'

    def fangzi(self):
        print("父亲的房子")

    def chezi(self):
        print("父亲的车子")

class Mother(object):

    def gongsi(self):
        print("母亲的公司")


class Sun(Father, Mother):

    def __init__(self):
        super().__init__()
        self.age = 20
        self.name = "zhangsan"


    def fangzi(self):
        super().fangzi()
        print("子类重写的房子")


if __name__ == '__main__':
    s = Sun()
    print(s.fangzi())
    print(s.chezi())
    print(s.gongsi())
    print(s.age)
    print(s.name)
    print(s.address)
