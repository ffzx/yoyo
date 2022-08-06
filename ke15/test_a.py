def setup_module():
    print("setup_module  整个py文件只执行一次")


class TestDemo(object):

    def setup_class(self):
        print("Demo1 setup_class  整个class 用例 之前，只执行一次")

    def setup(self):
        print("Demo1 setup  Demo1每个用例都会执行")

    def test_1(self):
        """用例1"""
        print("case 111")
        assert 1 == 1

    def test_2(self):
        """用例1"""
        print("case 222")
        assert 1 == 1


class TestDemo2(object):

    def setup_class(self):
        print("Demo2 setup_class  整个class 用例 之前，只执行一次")

    def setup(self):
        print("Demo2 setup 每个用例都会执行")

    def test_3(self):
        """用例1"""
        print("case 333")
        assert 1 == 1

    def test_4(self):
        """用例1"""
        print("case 444")
        assert 1 == 1
