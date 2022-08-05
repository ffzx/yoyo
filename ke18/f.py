class Father(object):

    def fangzi(self):
        print("父亲的房子")

    def chezi(self):
        print("父亲的车子")

class Mother(object):

    def gongsi(self):
        print("母亲的公司")


class Sun(Father, Mother):
    pass


if __name__ == '__main__':
    s = Sun()
    print(s.fangzi())
    print(s.chezi())
    print(s.gongsi())
