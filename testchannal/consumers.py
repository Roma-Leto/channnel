import channels
from asgiref.sync import async_to_sync
from channels.exceptions import StopConsumer
from channels.generic.websocket import WebsocketConsumer, SyncConsumer
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

    def websocket_connect(self, event):
        # Called on connection.
        # To accept the connection call:
        async_to_sync(self.channel_layer.group_add)(
            "broadcast",
            self.channel_name
        )
        self.accept()

        for i in range(5):
            self.send(json.dumps({'message': randint(1, 100)}))
            sleep(1)
        self.send(json.dumps({'message': event}))
        print('WebSocket connected....', event)

    def websocket_receive(self, event):
        """
        Called when a WebSocket frame is received. Decodes it and passes it
        to receive().
        """
        if "text" in event:
            print('EVENT', event)
            self.receive(text_data=event["text"])
            self.send(json.dumps({'message': event}))
        else:
            print('EVENT else ', event)
            self.receive(bytes_data=event["bytes"])
            self.send(json.dumps({'message': event}))
        print('WebSocket received....', event)

    def websocket_disconnect(self, event):
        """
        Called when a WebSocket connection is closed. Base level so you don't
        need to call super() all the time.
        """
        print('WebSocket disconnected....', event)
        raise StopConsumer()


