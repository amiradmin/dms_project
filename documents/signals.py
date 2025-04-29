# documents/signals.py
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

def notify_document_created_or_updated(instance):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "documents",
        {
            "type": "document.update",
            "message": {
                "id": instance.id,
                "title": instance.title,
                "updated": True,
            }
        }
    )
