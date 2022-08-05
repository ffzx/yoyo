def setup_module():
    print("整个py文件只执行一次")



class TestDemo(object):

    def setup_class(self):
        print("整个class 用例 之前，只执行一次")

    def setup(self):
        print("每个用例都会执行")

    def test_1(self):
        """用例1"""
        print("case 11111111")
        assert 1 == 1

    def test_2(self):
        """用例1"""
        print("case 11111111")
        assert 1 == 1


class TestDemo2(object):

    def setup_class(self):
        print("整个class 用例 之前，只执行一次")

    def setup(self):
        print("每个用例都会执行")

    def test_3(self):
        """用例1"""
        print("case 11111111")
        assert 1 == 1

    def test_4(self):
        """用例1"""
        print("case 11111111")
        assert 1 == 1

