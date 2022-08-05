res = {
    "code": 0,
    "msg": "success",
    "data": {
        "user": "text",
        "token": "xxxxxx1111111111111"
    }
}

print(res["code"])
print(res["msg"])
# token
print(res["data"]["token"])    # KeyError: 'token'  字典没有这个Key