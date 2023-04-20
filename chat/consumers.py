import json
from .models import Message
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):

	@database_sync_to_async
	def create_message(self, room_name, sender, message):
		return Message.objects.create(room_id=room_name, sender_id=sender, message=message)

	async def connect(self):
		self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
		self.room_group_name = self.room_name

		# Join room group
		await self.channel_layer.group_add(self.room_group_name, self.channel_name)

		await self.accept()

	async def disconnect(self, close_code):
		# Leave room group
		await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

	# Receive message from WebSocket
	async def receive(self, text_data):
		text_data_json = json.loads(text_data)
		username = text_data_json["username"]
		message = text_data_json["message"]

		await self.create_message(self.room_name, username, message)

		# Send message to room group
		await self.channel_layer.group_send(
			self.room_group_name, 
			{
				"type": "chat_message",
				"message": message,
				"username" : username
			}
		)

	# Receive message from room group
	async def chat_message(self, event):
		username = event['username']
		message = event['message']

		# Send message to WebSocket
		await self.send(text_data=json.dumps(
			{
				'message': message,
				'username' : username
			}
		))
