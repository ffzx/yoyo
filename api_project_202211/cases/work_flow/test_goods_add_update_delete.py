"""
流程类的接口用例
"""
from api.goods_api import add_goods, update_goods, get_goods
import time


def test_work_flow(login_fixture, base_url):
    """登录-添加商品-修改商品-查询商品"""
    sp_code = 'sp_' + str(int(time.time()))
    # 1.添加商品
    r1 = add_goods(login_fixture, base_url, sp_code, "测试商品")
    print(r1.text)
    sp_id = r1.json()['data']['id']
    print(f"获取到的商品id: {sp_id}")
    # 2.修改商品
    r2 = update_goods(login_fixture, base_url, sp_id, sp_code, '修改商品')
    print(r2.text)
    # 3.查询商品
    r3 = get_goods(login_fixture, base_url, sp_id)
    print(r3.text)
    assert r3.json()['code'] == 0
    assert r3.json()['data']['goodsname'] == '修改商品'