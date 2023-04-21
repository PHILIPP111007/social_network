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

	def create_chat(self, *args):
		a = min(*args)
		b = max(*args)
		room_name = f'{a}_{b}'
		if not self.__class__.objects.filter(room_name=room_name):
			self.room_name = room_name
			self.user_1 = a
			self.user_2 = b
			self.save()


class Message(models.Model):
	room_name = models.ForeignKey(Room, to_field='room_name', db_column='room_name', on_delete=models.CASCADE)
	sender = models.ForeignKey(User, to_field='username', db_column='username', on_delete=models.DO_NOTHING)
	message = models.CharField(max_length=1000)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.sender}: {self.message} [{self.timestamp}]'
