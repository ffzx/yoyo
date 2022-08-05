import requests
import json
url = "http://www.example.com"

queryString = {
    "a": "123",
    "c": "hello",
    "d": json.dumps({"key1": "value1","key2": "value2"})}
print(queryString)

r = requests.get(url, params=queryString)
