import jsonpath

result = {
    "code": 0,
    "msg": "success",
    "data": [
        {
            "age": 20,
            "name": "xx"
         },
          {
            "age": 22,
            "name": "cc"
         },
           {
            "age": 24,
            "name": "dd"
         }
    ]
}

code = jsonpath.jsonpath(result, '$.code')
print(code)
msg = jsonpath.jsonpath(result, '$.msg')
print(msg)
name = jsonpath.jsonpath(result, '$..name')
print(name)

# 取出年龄大于20的
age = jsonpath.jsonpath(result, '$.data[?(@.age > 20)]')
print(age)
# 根据条件过滤取值
name_age = jsonpath.jsonpath(result, '$.data[?(@.name == "xx")].age')
print(name_age)