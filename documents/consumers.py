from channels.generic.websocket import AsyncWebsocketConsumer
import json

class DocumentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("documents", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("documents", self.channel_name)

    async def document_update(self, event):
        await self.send(text_data=json.dumps(event["message"]))