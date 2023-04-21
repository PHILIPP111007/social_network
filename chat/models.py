from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
	room_name = models.CharField(max_length=1000, primary_key=True)
	user_1 = models.CharField(max_length=500)
	user_2 = models.CharField(max_length=500)
	delete_user_1 = models.CharField(max_length=500, default='0')
	delete_user_2 = models.CharField(max_length=500, default='0')

	def __str__(self):
		return self.room_name

	def create_chat(self, request_user, friend):
		a = min(request_user, friend)
		b = max(request_user, friend)
		room_name = f'{a}_{b}'

		room = self.__class__.objects.get(room_name=room_name, user_1=a, user_2=b)

		if a == request_user and room.delete_user_1 != '0':
			room.delete_user_1 = '0'
		elif b == request_user and room.delete_user_2 != '0':
			room.delete_user_2 = '0'

		room.save()


class Message(models.Model):
	room_name = models.ForeignKey(Room, to_field='room_name', db_column='room_name', on_delete=models.CASCADE)
	sender = models.ForeignKey(User, to_field='username', db_column='username', on_delete=models.DO_NOTHING)
	message = models.CharField(max_length=1000)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.sender}: {self.message} [{self.timestamp}]'
