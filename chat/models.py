from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
	user_1 = models.CharField(max_length=30)
	user_2 = models.CharField(max_length=30)
	delete_user_1 = models.CharField(max_length=30, default='0')
	delete_user_2 = models.CharField(max_length=30, default='0')
	
	def __str__(self):
		return f'{self.pk}: {self.user_1}_{self.user_2}'

	def create_chat(self, request_user, friend):
		a = min(request_user, friend)
		b = max(request_user, friend)

		room = self.__class__.objects.filter(user_1=a, user_2=b)

		if room:
			room = room[0]
			if a == request_user:
				if room.delete_user_1 != '0':
					room.delete_user_1 = '0'
					room.save(update_fields=['delete_user_1'])
				elif room.user_1 == '0':
					room.user_1 = request_user
					room.save(update_fields=['user_1'])

			elif b == request_user:
				if room.delete_user_2 != '0':
					room.delete_user_2 = '0'
					room.save(update_fields=['delete_user_2'])
				elif room.user_2 == '0':
					room.user_2 = request_user
					room.save(update_fields=['user_2'])
		else:
			room = self.__class__.objects.create(user_1=a, user_2=b)
		
		return room.pk


class Message(models.Model):
	room_name = models.ForeignKey(Room, to_field='id', db_column='room_name', on_delete=models.CASCADE)
	sender = models.ForeignKey(User, to_field='username', db_column='sender', on_delete=models.CASCADE)
	message = models.CharField(max_length=5000)
	timestamp = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering=['timestamp']

	def get_str_time(self, msg):
		time = msg.timestamp.strftime('%Y-%m-%d %H:%M')
		return time
		
	def __str__(self):
		return f'{self.room_name} [{self.timestamp}]'
