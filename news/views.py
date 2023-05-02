from django.shortcuts import render
from django.http import HttpResponseRedirect
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

    obj = Subscriber()
    friends = obj.get_friends(username=request.user.username)
    friends_records = Blog.objects.filter(user_id__in=friends) # .order_by('-date_time')
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
