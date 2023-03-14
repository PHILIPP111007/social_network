from django.db import models


class Room(models.Model):
	room_name = models.CharField(max_length=128, primary_key=True)
	user_1 = models.CharField(max_length=128)
	user_2 = models.CharField(max_length=128)

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
	
	def find_all_chats(self, username):
		chats = self.__class__.objects.filter(room_name__contains=username)
		"""
		a = chats[0]
		if username == a.user_1:
			return chats.values_list('user_2', flat=True)
		else:
			return chats.values_list('user_1', flat=True)
		"""
		return chats

"""
from django.contrib.auth.models import User
from django.db import models


class Room(models.Model):
	name = models.CharField(max_length=128)
	online = models.ManyToManyField(to=User, blank=True)

	def get_online_count(self):
		return self.online.count()

	def join(self, user):
		self.online.add(user)
		self.save()

	def leave(self, user):
		self.online.remove(user)
		self.save()

	def __str__(self):
		return f'{self.name} ({self.get_online_count()})'


class Message(models.Model):
	user = models.ForeignKey(to=User, on_delete=models.CASCADE)
	room = models.ForeignKey(to=Room, on_delete=models.CASCADE)
	content = models.CharField(max_length=512)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.user.username}: {self.content} [{self.timestamp}]'

"""
