d1 = {
    "a": None,
    "b": 1,
    "f": {"key": "value"},
    "c": "12a",
    "d": True,
    "e": ["1", 12],
}
print(d1)

# 1.新增一组 key=value
d1["h"] = "hello"
print(d1)
new = {"k": "v", "k1": "v1"}
d1.update(new)  # update 是新增一组字典
print(d1)

# 2.删除一组
del d1["b"]
print(d1)

# 3.修改 (有key就是修改)
d1["c"] = "a23"
print(d1)

# 4.查询 f
# print(d1["f1"])    # KeyError: 'f1'

# 判断有没有这个key,如果有，我们取值，没有给默认值
print(d1.get('f1', ''))

