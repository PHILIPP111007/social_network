from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
	user = models.ForeignKey(User, to_field='username', db_column='user', on_delete=models.CASCADE)
	date_time = models.DateTimeField(auto_now_add=True)
	content = models.TextField(max_length=5000)
	is_changed = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username


class Subscriber(models.Model):
	user = models.ForeignKey(User, related_name='user_1', to_field='username', db_column='user', on_delete=models.CASCADE) # models.ForeignKey(User, related_name='user', db_column='username', on_delete=models.CASCADE)  # to_field='username', db_column='username',
	subscribe = models.ForeignKey(User, related_name='user_2', to_field='username', db_column='subscribe', on_delete=models.CASCADE) # models.ForeignKey(User, related_name='subscribe', db_column='username', on_delete=models.CASCADE) # CharField(max_length=20)

	def __str__(self):
		return self.user.username

	def get_friends(self, username):

		set_1 = set(self.__class__.objects.filter(user=username).values_list('subscribe', flat=True))
		set_2 = set(self.__class__.objects.filter(subscribe=username).values_list('user', flat=True))

		friends_set = set_1 & set_2
		friends = User.objects.filter(username__in=friends_set)

		subscriptions_set = set_1 - set_2
		subscriptions = User.objects.filter(username__in=subscriptions_set)

		subscribers_set = set_2 - set_1
		subscribers = User.objects.filter(username__in=subscribers_set)

		return friends, subscriptions, subscribers


class UserSettings(models.Model):
	user = models.OneToOneField(User, to_field='username', db_column='user', on_delete=models.CASCADE, primary_key=True)
	low_power_mode = models.BooleanField(default=True)

	def __str__(self):
		return self.user.username
	