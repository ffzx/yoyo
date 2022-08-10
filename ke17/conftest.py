import pytest
import requests
from ke17.api.login_api import login

"""
连接数据库
"""
@pytest.fixture(scope="session")
def requests_session():
    """创建session会话"""
    s = requests.Session()
    yield s
    s.close()  # 后置操作


@pytest.fixture(scope="session")
def login_fixture(requests_session):
    """前置登录"""
    login(requests_session, username="test11", password="123456")
    return requests_session

