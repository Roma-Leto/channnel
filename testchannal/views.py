import websocket
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.shortcuts import render

import testchannal.consumers


def index(request):
    context = {
        'text': 'text'
    }
    return render(request, 'index.html', context)


def dataset(request, ddata):
    context = {
        'data': ddata
    }
    print('data: ', ddata)
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)("broadcast", {'message': str(ddata)})
    return render(request, 'data.html', context)
