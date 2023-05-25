from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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
