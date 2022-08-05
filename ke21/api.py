import allure


@allure.step("步骤：添加商品")
def step1():
    print("步骤111111111")


@allure.step("步骤：修改商品")
def step2():
    print("步骤222222222222222")


@allure.step("步骤：查询商品")
def step3():
    print("步骤33333333333")