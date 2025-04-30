# documents/routing.py

from django.urls import re_path
from . import consumers
from typing import List

# Define the URL routing for WebSocket connections in the documents app
websocket_urlpatterns: List[re_path] = [
    re_path(r'ws/documents/$', consumers.DocumentConsumer.as_asgi()),
]
