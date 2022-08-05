"""
self 是类本身的实例对象
我自己  myself
"""

class People(object):

   def chifan(self):
       """方法是行为的描述"""
       print("吃饭。。。。。")

   def zoulu(self):
       """走路"""
       print("走路。。。。。")

   def chibaozi(self):
       self.zoulu()  # 自己调用自己的方法
       print('吃包子')




if __name__ == '__main__':
   zhangsan = People()
   zhangsan.chibaozi()
