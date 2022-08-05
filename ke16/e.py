"""
参数组合的情况（笛卡尔积）
"""
import pytest


@pytest.mark.parametrize('x', [0, 1])
@pytest.mark.parametrize('y', [2, 3])
def test_foo(x, y):
    print(f"参数组合x->{x}, y->{y}")
    # 期望结果只能有一个固定，传expected
