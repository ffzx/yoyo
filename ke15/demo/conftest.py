import pytest
import requests
from ke15.api.login_api import login


@pytest.fixture(scope="session")
def requests_session():
    """创建session会话"""
    s = requests.Session()
    yield s
    s.close()  # 后置操作


@pytest.fixture(scope="session")
def login_fixture(requests_session):
    """登录"""
    login(requests_session, username="test11", password="123456")
    return requests_session

