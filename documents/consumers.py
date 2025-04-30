from channels.generic.websocket import AsyncWebsocketConsumer
import json
from typing import Any, Dict


class DocumentConsumer(AsyncWebsocketConsumer):
    """
    WebSocket consumer for real-time document notifications.
    Listens to the 'documents' channel group and sends updates to connected clients.
    """

    async def connect(self) -> None:
        """
        Called when a WebSocket connection is established.
        Adds the client to the 'documents' channel group.
        """
        await self.channel_layer.group_add("documents", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code: int) -> None:
        """
        Called when the WebSocket connection is closed.
        Removes the client from the 'documents' channel group.
        """
        await self.channel_layer.group_discard("documents", self.channel_name)

    async def document_update(self, event: Dict[str, Any]) -> None:
        """
        Handles 'document.update' events and sends the message to the WebSocket client.
        :param event: Dictionary containing the message payload
        """
        await self.send(text_data=json.dumps(event["message"]))
