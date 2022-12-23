import websocket
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.http import HttpResponse
from django.shortcuts import render

import testchannal.consumers


def index(request):
    context = {
        'text': 'text'
    }
    return render(request, 'index.html', context)


def dataset(request, ddata):
    channel_layer = get_channel_layer()
    # print(channel_layer)
    async_to_sync(channel_layer.group_send)(
        "broadcast",
        {
            'type': 'websocket_receive',
            'message': str(ddata),
            'bytes': 4,
        }
    )

    context = {
        'data': ddata
    }
    print('data: ', ddata)
    return HttpResponse(f'Message {context} =)')
