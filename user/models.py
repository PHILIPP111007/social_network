from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q


class Blog(models.Model):
	user = models.ForeignKey(User, to_field="username", db_column="user", on_delete=models.CASCADE)
	date_time = models.DateTimeField(auto_now_add=True)
	content = models.TextField(max_length=5000)
	is_changed = models.BooleanField(default=False)

	class Meta:
		ordering=["-date_time"]

	def __str__(self):
		return self.user.username


class Subscriber(models.Model):
	user = models.ForeignKey(User, related_name="user_1", to_field="username", db_column="user", on_delete=models.CASCADE)
	subscribe = models.ForeignKey(User, related_name="user_2", to_field="username", db_column="subscribe", on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username

	@staticmethod
	def get_friends(username):
		set_1 = Subscriber.objects.filter(user=username).values_list("subscribe", flat=True)
		set_2 = Subscriber.objects.filter(subscribe=username).values_list("user", flat=True)
		friends = User.objects.filter(
			Q(username__in=set_1) & Q(username__in=set_2)
		)
		return friends

	@staticmethod
	def get_friends_subscriptions_subscribers(username):
		set_1 = Subscriber.objects.filter(user=username).values_list("subscribe", flat=True)
		set_2 = Subscriber.objects.filter(subscribe=username).values_list("user", flat=True)

		friends = User.objects.filter(
			Q(username__in=set_1) & Q(username__in=set_2)
		)
		subscriptions = User.objects.filter(
			Q(username__in=set_1) & ~Q(username__in=set_2)
		)
		subscribers = User.objects.filter(
			Q(username__in=set_2) & ~Q(username__in=set_1)
		)
		return friends, subscriptions, subscribers


class UserSettings(models.Model):
	user = models.OneToOneField(User, to_field="username", db_column="user", on_delete=models.CASCADE, primary_key=True)
	low_power_mode = models.BooleanField(default=True)
	theme = models.BooleanField(default=True)  # True = light theme, False = dark theme

	class Meta:
		verbose_name_plural = "UserSettings"

	def __str__(self):
		return self.user.username
