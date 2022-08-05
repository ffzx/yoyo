from ke15.api.userinfo_api import add_userinfo, get_userinfo
import jsonpath


def test_case(login_fixture):
    """流程性的用例"""
    # step 1 需要修改
    r = add_userinfo(login_fixture, mail="222@qq.com")
    print(r.text)
    # step2 查询
    r2 = get_userinfo(login_fixture)
    print(r2.text)
    mail = jsonpath.jsonpath(r2.json(), '$..mail')[0]
    assert mail == "222@qq.com"
