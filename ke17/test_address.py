"""
添加address
"""

import requests
from ke17.db_connect import DBConnect, dbinfo
import time


def select_db(sql):
    db = DBConnect(dbinfo=dbinfo, database="apps")
    res = db.select(sql)
    db.close()
    return res


def test_address(login_fixture):
    """收获地址，手机号添加"""
    url = 'http://49.235.92.12:7005/api/v2/address'
    body = {"tel": "15001234003"}
    r = login_fixture.post(url, json=body)
    print(r.text)
    acturl_tel = r.json()['data']['tel']
    print(acturl_tel)
    # 期望结果
    sql = "SELECT * from apiapp_useraddress WHERE userid='test11';"
    time.sleep(2)
    expected = select_db(sql)
    print(expected)
    assert acturl_tel == expected[0]['tel']
