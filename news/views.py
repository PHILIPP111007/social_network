from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User
from user.models import Blog, Subscriber, UserSettings


POSTS_TO_DOWNLOAD = 20

@login_required
def index(request, username):
	user = User.objects.get(username=request.user.username)
	settings = UserSettings.objects.get(user_id=request.user.username)

	result_dict = {
		'user': user,
		'settings': settings,
		'posts_to_download': POSTS_TO_DOWNLOAD
	}
	return render(request, 'news.html', result_dict)


def lazy_loader(request, username, posts_number):

	is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
	if is_ajax and request.method == 'GET':

		friends = Subscriber.get_friends(username=request.user.username)
		friends_records = Blog.objects.filter(user_id__in=friends)[posts_number:posts_number + POSTS_TO_DOWNLOAD].values()

		result = [item for item in friends_records]

		for item in result:
			user = User.objects.get(username=item["user_id"])
			item['first_name'] = user.first_name
			item['last_name'] = user.last_name
			item['date_time'] = item['date_time'].strftime('%Y-%m-%d %H:%M')
		
		if result:
			return JsonResponse({
				'status': True,
				'friends_records': result
			})
	return JsonResponse({'status': False})
