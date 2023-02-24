from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from user.models import Blog, Subscriber


def index(request, username):
    if request.user.is_authenticated:
        
        result_dict = make_content(request)
        return render(request, 'news.html', result_dict)
    else:
        return HttpResponseRedirect('/social_network/auth')



def make_content(request):

    user = User.objects.get(username=request.user.username)

    obj = Subscriber()
    my_friends = obj.get_friends(username=request.user.username)
    friends_records = Blog.objects.filter(user_id__in=my_friends).order_by('-date_time')

    result_dict = {
		'is_my_page': True,
		'name': user.first_name,
		'surname': user.last_name,
		'nickname': user.username,
        'friends_records': friends_records
	}
    return result_dict


def quit(request, username):

    if request.method == 'GET' and request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/social_network/auth')
