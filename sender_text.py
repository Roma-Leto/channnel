import requests
import os

while 1:
    # params = {'data': 'value1', 'key2': 'value2'}
    mes = input('Введите сообщение:')
    # resp = requests.get('http://127.0.0.1:8000/data', params=params)
    resp = requests.get(f'http://127.0.0.1:8000/data/{mes}')
    print(resp.url)
    os.system('CLS')



# import channels
#
# from websocket import create_connection
# from asgiref.sync import async_to_sync
#
#
# ws = create_connection("ws://localhost:8000/ws/some_url/")
#
# print(ws.recv())
# print("Sending 'Hello, World'...")
# ws.send("Hello, World")
# print("Sent")
# print("Receiving...")
# result = ws.recv()
# print("Received '%s'" % result)
# ws.close()
