import pytest
from channels.testing import WebsocketCommunicator
from config.asgi import application

@pytest.mark.asyncio
@pytest.mark.django_db
async def test_notification_socket_connects():
    communicator = WebsocketCommunicator(application, "/ws/notifications/")
    connected, _ = await communicator.connect()
    assert connected
    await communicator.disconnect()
