from django.db import models
from django.contrib.auth.models import User




class MyUser(models.Model):
	username = models.CharField(primary_key=True, max_length=20)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)

	def __str__(self):
		return self.username



class Blog(models.Model):
	user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
	date_time = models.DateTimeField(auto_now_add=True)
	content = models.TextField()
	is_changed = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username




class Subscriber(models.Model):
	user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
	subscriber = models.CharField(max_length=20)

	def __str__(self):
		return self.user.username


	def get_friends(self, username):
		lst_1 = self.__class__.objects.filter(user_id=username).values_list('subscriber')
		lst_2 = self.__class__.objects.filter(subscriber=username).values_list('user_id')
		lst = []
		for person in lst_1:
			if person in lst_2:
				lst.append(MyUser.objects.get(username=person[0]))
		friends = MyUser.objects.filter(username__in=lst)

		return friends

	
	def get_subscriptions(self, username):
		friends = self.get_friends(username)

		subscriptions_list = self.__class__.objects.filter(user_id=username).values_list('subscriber')
		subscriptions = MyUser.objects.filter(username__in=subscriptions_list)
		subscriptions = subscriptions.exclude(username__in=friends)

		return subscriptions
		
	
	def get_subscribers(self, username):
		friends = self.get_friends(username)

		subscribers_list = self.__class__.objects.filter(subscriber=username).values_list('user_id')
		subscribers = MyUser.objects.filter(username__in=subscribers_list)
		subscribers = subscribers.exclude(username__in=friends)

		return subscribers



