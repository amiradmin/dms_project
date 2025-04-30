# documents/signals.py

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from documents.models import Document


def notify_document_created_or_updated(instance: Document) -> None:
    """
    Notify all subscribed WebSocket clients that a document was created or updated.

    Args:
        instance (Document): The document instance that was created or updated.

    Sends:
        A message to the 'documents' group via Django Channels with the document's ID and title.
    """
    channel_layer = get_channel_layer()

    if not channel_layer:
        return  # Channel layer not configured or available

    async_to_sync(channel_layer.group_send)(
        "documents",
        {
            "type": "document.update",  # This should match the method name in the consumer
            "message": {
                "id": instance.id,
                "title": instance.title,
                "updated": True,
            }
        }
    )
