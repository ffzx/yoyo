"""
添加商品
修改商品
查询商品
删除商品
"""
from requests import Session, Response


def add_goods(s:Session, base_url, goods_code, goods_name, **kwargs)->Response:
    url = base_url + "/api/v2/goods"
    body = {
        "goodsname": goods_name,
        "goodscode": goods_code
    }
    body.update(kwargs)
    return s.post(url, json=body)


def update_goods(s, base_url, id, goods_code, goods_name, **kwargs) ->Response:
    url = base_url + '/api/v2/goods/{}'.format(id)
    body = {
        "goodsname": goods_name,
        "goodscode": goods_code,  # 跟id 一一对应
    }
    body.update(kwargs)
    return s.put(url, json=body)


def get_goods(s, base_url, sp_id) -> Response:
    """查询商品"""
    url = base_url + '/api/v2/goods/{}'.format(sp_id)
    return s.get(url)
