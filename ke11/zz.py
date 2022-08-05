import re
"""
正则取值对象，只能是字符串
jsonpath取值对象 dict
"""

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
import json
res = json.dumps(result)
print(res)

# 正则取值
msg = re.findall('"msg": "(.+?)"', res)
print(msg)  # ['success']