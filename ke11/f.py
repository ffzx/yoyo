import json

# json 不是基础的数据类型    str list tuple dict

a = {
    'name': "yoyo",
    "mail": "123@qq.com",
    "age": "22",
    "tel": "12345678901"
}
print(a)  # {'name': 'yoyo', 'mail': '123@qq.com', 'age': '22', 'tel': '12345678901'}
print(type(a))
b = json.dumps(a)  # {"name": "yoyo", "mail": "123@qq.com", "age": "22", "tel": "12345678901"}
print(b)
print(type(b))  # json就是(有规律的)字符串

# json的规律
"""
1.json对象 严格的双引号  {"key": "value", "key11": "value2"}
2.json数组  ["a", "b1", 1, true, null, {"key": "value"}]
3.string
4.num
5.bool
7.null
"""

aa = ["a", "b1", 1, True, None, {"key": "value"}]
# 转json
bb = json.dumps(aa)
print(bb)  # ["a", "b1", 1, true, null, {"key": "value"}]

cc = '{"key": "value"}'   # json有规律的字符串


