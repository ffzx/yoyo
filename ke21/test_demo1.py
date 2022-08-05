from ke21.api import step1, step2, step3
import allure


@allure.feature("商品步骤演示")
class TestDemo():

    @allure.title("用例描述，多个步骤")
    def test_1(self):
        """多个步骤：
        1.步骤登录
        2.添加商品
        3.修改商品"""
        step1()
        step2()
        step3()



