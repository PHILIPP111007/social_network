from django.db import models
from django.contrib.auth.models import User



class Blog(models.Model):
	user = models.ForeignKey(User, to_field='username', db_column='username', on_delete=models.CASCADE)  # !!!!!
	date_time = models.DateTimeField(auto_now_add=True)
	content = models.TextField()
	is_changed = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username



class Subscriber(models.Model):
	user = models.ForeignKey(User, to_field='username', db_column='username', on_delete=models.CASCADE)
	subscriber = models.CharField(max_length=20)

	def __str__(self):
		return self.user.username


	def get_friends(self, username):

		lst_1 = self.__class__.objects.filter(user_id=username).values_list('subscriber', flat=True)
		lst_2 = self.__class__.objects.filter(subscriber=username).values_list('user', flat=True)

		friends_lst = list(set(lst_1) & set(lst_2))
		friends = User.objects.filter(username__in=friends_lst)

		subscriptions_lst = list(set(lst_1) - set(lst_2))
		subscriptions = User.objects.filter(username__in=subscriptions_lst)

		subscribers_lst = list(set(lst_2) - set(lst_1))
		subscribers = User.objects.filter(username__in=subscribers_lst)

		return friends, subscriptions, subscribers
