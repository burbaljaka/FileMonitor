from channels.generic.websocket import AsyncJsonWebsocketConsumer
import os


class DirChangeConsumer(AsyncJsonWebsocketConsumer):
    channel_layer_alias = "folder"

    async def connect(self):
        await self.accept()

    async def disconnect(self, code):
        pass

    async def reloader(self, message):
        print('WS message sent')
        await self.send_json(content=message)

    # async def reloader(self, event):
    #     await self.send_json(content=event['content'])

