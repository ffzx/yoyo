import json

# json 的数据格式
a = '{"key": "111", "name": "yy", "age": 11}'   # json 字符串 str
# json {} object
print(json.loads(a))
print(type(json.loads(a)))

b = '[2, "a", true, null]'  # json 字符串 str
print(json.loads(b))    # JSONDecodeError