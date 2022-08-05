import pytest

import os

import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture(scope="session")
def login_fixture():
    """前置：登录
    """
    print("登录---------")
