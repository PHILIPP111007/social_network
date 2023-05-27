from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from user.models import Blog, Subscriber, UserSettings
from social_network.settings import POSTS_TO_DOWNLOAD, TIME_PATTERN


@login_required
def index(request, username):
	user = User.objects.get(username=request.user.username)
	settings = UserSettings.objects.get(user_id=request.user.username)

	result_dict = {
		"user": user,
		"settings": settings,
		"posts_to_download": POSTS_TO_DOWNLOAD
	}
	return render(request, "news.html", result_dict)


@login_required
def lazy_loader(request, username, posts_number):

	is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"
	if is_ajax and request.method == "GET":

		friends = Subscriber.get_friends(username=request.user.username)
		friends_records = Blog.objects.filter(user_id__in=friends)[posts_number:posts_number + POSTS_TO_DOWNLOAD]

		if friends_records:
			result = [
				{
					'id': post.id,
					'user_id': post.user.username,
					'first_name': post.user.first_name,
					'last_name': post.user.last_name,
					'date_time': post.date_time.strftime(TIME_PATTERN),
					'content': post.content,
					'is_changed': post.is_changed
				} for post in friends_records
			]

			return JsonResponse({
				"status": True,
				"friends_records": result
			})
	return JsonResponse({"status": False})
