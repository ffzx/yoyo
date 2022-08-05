"""
object 是基类
每个类都需要继承一个类，如果没有，默认继承object
"""


class People(object):


   def chifan(self):
       """方法是行为的描述"""
       print("吃饭。。。。。")

   def zoulu(self):
       """走路"""
       print("走路。。。。。")

if __name__ == '__main__':
    # 实例化类
    people = People()
    print(people)
    # 实例方法 带（self)的方法叫实例方法
    people.chifan()
    people.zoulu()
    # 多个实例
    people2 = People()
    people2.chifan()
