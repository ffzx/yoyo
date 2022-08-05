"""
注册示例
http://49.235.92.12:7005/api/v1/register
"""
import requests
import pytest
from ke17.db_connect import DBConnect,dbinfo


@pytest.fixture(scope="function")
def delete_user():
    """前置删除数据"""
    db = DBConnect(dbinfo=dbinfo, database="apps")
    sql = 'DELETE from auth_user WHERE username="test1123";'
    db.execute(sql)
    db.close()


def test_register(delete_user):
    """注册"""
    url = "http://49.235.92.12:7005/api/v1/register"
    body = {
        "username": "test1123",
        "password": "123456",
        "mail": "1233@qq.com"
    }
    r = requests.post(url=url, json=body)
    print(r.text)
    assert r.json()['code'] == 0
    assert r.json()['msg'] == 'register success!'


def test_register_2():
    """重复注册"""
    url = "http://49.235.92.12:7005/api/v1/register"
    body = {
        "username": "test1123",
        "password": "123456",
        "mail": "1233@qq.com"
    }
    r = requests.post(url=url, json=body)
    r2 = requests.post(url=url, json=body)
    print(r2.text)
    assert r2.json()['code'] == 2000
    assert r.json()['msg'] == 'test1123用户已被注册'
