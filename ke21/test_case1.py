import allure


@allure.feature("添加商品")
class TestCase1():

    @allure.story("用户故事，添加商品成功")
    @allure.title("输入商品名称，输入code合法,保存成功")
    @allure.severity("blocker")
    def test_a1(self):
        print("a11111111111")

    @allure.story("用户故事，添加商品成功")
    @allure.title("输入重复商品名称，输入code合法,保存成功")
    @allure.severity("critical")
    def test_a2(self):
        print("2222222222222")

    @allure.story("添加商品失败场景")
    @allure.title("输入不合法商品名称，输入code合法,保存失败")
    def test_a3(self):
        print("33333333333333")

    @allure.severity("critical")
    def test_a4(self):
        print("2222222222222")
        assert 1 == 2

    def test_a5(self):
        print("2222222222222")
        assert 1 == 2
