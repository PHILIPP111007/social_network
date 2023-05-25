from django.urls import re_path
from chat import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/delete_message/(?P<room_name>\w+)/$', consumers.DeleteMessageConsumer.as_asgi())
]
