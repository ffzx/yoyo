"""
添加、修改用户信息参数用例
"""
from ke15.api.userinfo_api import add_userinfo


def test_add_info(login_fixture):
    """添加、修改用户信息参数用例"""
    print(login_fixture)  # Session object
    r = add_userinfo(login_fixture, "test11")
    print(r.text)
    assert r.json()['code'] == 0
    assert r.json()['message'] == 'update some data!'


def test_add_info_2(login_fixture):
    """添加、修改用户信息参数用例 无权限修改"""
    print(login_fixture)  # Session object
    r = add_userinfo(login_fixture, "test12")
    print(r.text)
    assert r.json()['code'] == 4003
    assert r.json()['message'] == '无权限操作'