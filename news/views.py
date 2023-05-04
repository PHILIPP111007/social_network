from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from user.models import Blog, Subscriber, UserSettings


@login_required
def index(request, username):
    result_dict = make_content(request)
    return render(request, 'news.html', result_dict)


def make_content(request):
    user = User.objects.get(username=request.user.username)

    friends = Subscriber().get_friends(username=request.user.username)
    friends_records = Blog.objects.filter(user_id__in=friends)
    settings = UserSettings.objects.get(user_id=request.user.username)

    result_dict = {
		'is_my_page': True,
        'user': user,
        'friends_records': friends_records,
        'settings': settings
	}
    return result_dict


def quit(request, username):
	if request.method == 'GET':
		logout(request)
	return HttpResponseRedirect('/')


@login_required
def background_color_change(request, username):
	is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

	if is_ajax and request.method == 'POST' and request.body:

		color = bool(int(request.body.decode('utf-8')))
		try:
			settings = UserSettings.objects.get(user_id=request.user.username)
			settings.theme = color
			settings.save(update_fields=['theme'])
			return JsonResponse({'status': True})
		except UserSettings.DoesNotExist:
			return JsonResponse({'status': False})
