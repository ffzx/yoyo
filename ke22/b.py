"""
http/https  https = http + ssl

ws/wss   wss = ws + ssl
"""
from websocket import create_connection
import json

ws = create_connection("ws://49.235.92.12:7005/test_websocket")
print(ws.getstatus())

while True:
    send_msg = input("输入发送内容:")
    ws.send(send_msg)
    res = ws.recv()
    print(res)  # json
    print(json.loads(res))