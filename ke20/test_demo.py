import pytest
import requests


def test_demo(base_url):
    """测试"""
    print(base_url)
    assert requests.get(base_url).status_code == 200