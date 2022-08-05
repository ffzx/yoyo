import pytest
"""
smoke: 冒烟测试
workflow: 流程测试
全量测试
"""


@pytest.mark.smoke
def test_login():
    print("login")


def test_login_fail():
    print("fail")


@pytest.mark.smoke
def test_register():
    print("register")


@pytest.mark.workflow
def test_work_flow():
    print("flow....")


@pytest.mark.workflow
def test_work_flow_2():
    print("flow....")