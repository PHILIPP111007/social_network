from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from user.models import Subscriber
from .forms import FindUser


def index(request, username):
    
    if request.user.is_authenticated:
        if request.method == 'GET':
            result_dict = make_content(request)
            return render(request, 'friends.html', result_dict)
        
        elif request.method == 'POST':
            find_users = find_user(request)
            result_dict = make_content(request, find_users=find_users)
            return render(request, 'friends.html', result_dict)
    else:
        return HttpResponseRedirect('/social_network/auth')



def make_content(request, find_users=None):

    user = User.objects.get(username=request.user.username)

    obj = Subscriber()
    friends = obj.get_friends(username=request.user.username)
    subscriptions = obj.get_subscriptions(username=request.user.username)
    subscribers = obj.get_subscribers(username=request.user.username)

    result_dict = {
		'first_name': user.first_name,
		'last_name': user.last_name,
		'username': user.username,
        'find_user_form': FindUser(),
        'find_users': find_users,
        'friends': friends,
        'subscriptions': subscriptions,
        'subscribers': subscribers,
	}

    if find_users:
        result_dict['find_users'] = result_dict['find_users'].exclude(username__in=friends)
        result_dict['find_users'] = result_dict['find_users'].exclude(username__in=subscriptions)
        result_dict['find_users'] = result_dict['find_users'].exclude(username__in=subscribers)

    return result_dict



def quit(request, username):

    if request.method == 'GET' and request.user.is_authenticated and request.user.username == username:
        logout(request)
        return HttpResponseRedirect('/social_network/auth')



def find_user(request):

    username = request.POST.get('username')

    if username != '':
        find_users = User.objects.filter(username=username)
    else:
        result_str = 'User.objects'

        first_name = request.POST.get('first_name')
        if first_name != '':
            result_str += f'.filter(first_name="{first_name}")'

        last_name = request.POST.get('last_name')
        if last_name != '':
            result_str += f'.filter(last_name="{last_name}")'


        if result_str != 'User.objects':
            find_users = eval(result_str)

    if find_users:
        find_users = find_users.exclude(username=request.user.username)
        return find_users



def add_friend(request, username):
    if request.method == 'POST':
        if request.user.is_authenticated:

            if not Subscriber.objects.filter(subscriber=username, user_id=request.user.username):
                Subscriber.objects.create(subscriber=username, user_id=request.user.username)
            
            return HttpResponseRedirect(f'/social_network/friends/{request.user.username}')
        else:
            return HttpResponseRedirect('/social_network/auth')



def delete_friend(request, username):
    if request.method == 'POST':
        if request.user.is_authenticated:
            
            try:
                subscriber = Subscriber.objects.get(subscriber=username, user_id=request.user.username)
                subscriber.delete()
            except Exception:
                pass

            return HttpResponseRedirect(f'/social_network/friends/{request.user.username}')
        else:
            return HttpResponseRedirect('/social_network/auth')

    

def delete_subscriber(request, username):
    if request.method == 'POST':
        if request.user.is_authenticated:
            
            try:
                subscriber = Subscriber.objects.get(subscriber=request.user.username, user_id=username)
                subscriber.delete()
            except Exception:
                pass

            return HttpResponseRedirect(f'/social_network/friends/{request.user.username}')
        else:
            return HttpResponseRedirect('/social_network/auth')
