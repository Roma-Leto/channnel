import requests
import os

while 1:
    # params = {'data': 'value1', 'key2': 'value2'}
    mes = input('Введите сообщение:\n')
    # resp = requests.get('http://127.0.0.1:8000/data', params=params)
    # try:
    #     resp = requests.get(f'http://127.0.0.1:8000/data/{mes}')
    # except:
    #     pass
    try:
        resp = requests.get(f'http://192.168.1.3:80/data/{mes}')
    except:
        pass
    # print(resp.url)
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
