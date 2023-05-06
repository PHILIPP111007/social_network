import json
from .models import Message
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):

	@database_sync_to_async
	def create_message(self, room_name, sender, message):
		return Message.objects.create(room_name_id=room_name, sender_id=sender, message=message)

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
		first_name = text_data_json["first_name"]
		last_name = text_data_json["last_name"]
		message = text_data_json["message"]

		message_obj = await self.create_message(self.room_name, username, message)

		timestamp = Message().get_str_time(message_obj)

		# Send message to room group
		await self.channel_layer.group_send(
			self.room_group_name, 
			{
				"type": "chat_message",
				"message": message,
				"message_id": message_obj.id,
				"username" : username,
				"first_name": first_name,
				"last_name": last_name,
				"timestamp": timestamp
			}
		)

	# Receive message from room group
	async def chat_message(self, event):
		username = event['username']
		message = event['message']
		message_id = event['message_id']
		first_name = event['first_name']
		last_name = event['last_name']
		timestamp = event['timestamp']

		# Send message to WebSocket
		await self.send(text_data=json.dumps(
			{
				'message': message,
				"message_id": message_id,
				'username' : username,
				"first_name": first_name,
				"last_name": last_name,
				"timestamp": timestamp
			}
		))
