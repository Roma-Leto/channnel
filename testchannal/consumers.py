import channels
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from time import sleep
import channels.layers
from random import randint


# class WSConsumer(WebsocketConsumer):
#     groups = ["broadcast"]
    # # def connect(self):
    # #     self.accept()
    # #
    # #     for i in range(5):
    # #         self.send(json.dumps({'message': randint(1, 100)}))
    # #         sleep(1)
    #
    # # def connect(self):
    # #
    # #     channel_layer = channels.layers.get_channel_layer()
    # #     print('self.channel_layer', self.channel_layer)
    # #     print('channel_layer', channel_layer)
    # #     print(self.channel_name)
    # #     self.send(json.dumps({'message': randint(1, 100)}))
    # #     self.accept()
    #
    # def websocket_connect(self, event):
    #     self.accept({
    #         'type': 'websocket.accept'
    #     })
    #     for i in range(5):
    #         self.send(json.dumps({'message': randint(1, 100)}))
    #         sleep(1)
    #
    #     print('CONNECTED')
    #
    # #
    # # def receive(self, text_data):
    # #     print('consum 19 ', text_data)
    # #     self.send(json.dumps({'message': text_data}))
    #
    # def disconnect(self, event):
    #     print('DISCONNECTED!')
    #
    # def receive(self, text_data=None, bytes_data=None):
    #
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json["message"]
    #
    #     if "Hello" in message:
    #         self.receive(text_data=message["text"])
    #     else:
    #         self.receive(bytes_data=message["bytes"])
    #
    #     self.send(text_data=json.dumps({"message": message}))


class WSConsumer(WebsocketConsumer):
    groups = ["broadcast"]

    def connect(self):
        # Called on connection.
        # To accept the connection call:
        self.accept()

        for i in range(5):
            self.send(json.dumps({'message': randint(1, 100)}))
            sleep(1)
        # Or accept the connection and specify a chosen subprotocol.
        # A list of subprotocols specified by the connecting client
        # will be available in self.scope['subprotocols']
        # self.accept("subprotocol")
        # To reject the connection, call:

        # self.close()

    def receive(self, text_data=None, bytes_data=None):
        # Called with either text_data or bytes_data for each frame
        # You can call:
        self.send(text_data="Hello world!")
        # Or, to send a binary frame:
        self.send(bytes_data="Hello world!")
        # Want to force-close the connection? Call:
        self.close()
        # Or add a custom WebSocket error code!
        self.close(code=4123)

    def disconnect(self, close_code):
        print('DISCONNECTED!')

