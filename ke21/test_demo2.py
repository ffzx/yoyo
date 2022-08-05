from yoyoketang.ke21.api_new import step1, step2, step3
import allure


@allure.feature("商品步骤演示")
class TestDemo2():

    @allure.title("用例描述，多个步骤2222")
    @allure.testcase("http://49.235.92.12:8080/zentao/testcase-view-644-1.html")
    @allure.issue("http://49.235.92.12:8080/zentao/bug-view-43.html")
    def test_222(self, login_fixture):
        """多个步骤：
        1.步骤登录
        2.添加商品
        3.修改商品"""
        with allure.step("步骤1：添加商品"):
            step1()
        with allure.step("步骤2：修改商品"):
            step2()
        with allure.step("步骤3：查询商品"):
            step3()


