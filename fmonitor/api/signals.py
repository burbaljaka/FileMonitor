from django.dispatch import Signal, receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import os

reload_dir = Signal(providing_args=['path'])


@receiver(reload_dir)
def initiate_ws(path, **kwargs):
    files = {}
    files['data'] = [f for f in os.listdir(path)]
    print('Signal passes')
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.send)(
        'folder',
        {
            'type': 'reloader',
            'message': files
        }
    )