"""
2个账号同时登录操作
a账号做A事情
b账号做B事情
a再做其他事
"""
import requests

s1 = requests.Session()  # s1

s2 = requests.Session()  # s2
