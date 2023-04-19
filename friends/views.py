from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from user.models import Subscriber
from chat.models import Room


@login_required
def index(request, username):
    if request.method == 'GET':
        result_dict = make_content(request)
        return render(request, 'friends.html', result_dict)
    elif request.method == 'POST':
        find_users = find_user(request)
        result_dict = make_content(request, find_users=find_users)
        return render(request, 'friends.html', result_dict)


def make_content(request, find_users=None):
    user = User.objects.get(username=request.user.username)
    obj = Subscriber()
    friends, subscriptions, subscribers = obj.get_friends(username=request.user.username)

    result_dict = {
        'user': user,
        'find_users': find_users,
        'friends': friends,
        'subscriptions': subscriptions,
        'subscribers': subscribers,
	}
    if find_users:
        result_dict['find_users'] = result_dict['find_users'].exclude(username__in=friends.values_list('username'))
        result_dict['find_users'] = result_dict['find_users'].exclude(username__in=subscriptions.values_list('username'))
        result_dict['find_users'] = result_dict['find_users'].exclude(username__in=subscribers.values_list('username'))

    return result_dict


def quit(request, username):
    logout(request)
    return HttpResponseRedirect('/social_network')


def find_user(request):
    username = request.POST.get('username')
    find_users = ''

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


@login_required
def add_friend(request, username):
    if request.method == 'POST':
        if not Subscriber.objects.filter(subscribe=username, user_id=request.user.username):
            Subscriber.objects.create(subscribe=username, user_id=request.user.username)
            
        return HttpResponseRedirect(f'/social_network/friends/{request.user.username}')


@login_required
def delete_friend(request, username):
    if request.method == 'POST':
        try:
            subscribe = Subscriber.objects.get(subscribe=username, user_id=request.user.username)
            subscribe.delete()
        except Exception:
            pass

        return HttpResponseRedirect(f'/social_network/friends/{request.user.username}')


@login_required
def delete_subscriber(request, username):
    if request.method == 'POST':
        try:
            subscribe = Subscriber.objects.get(subscribe=request.user.username, user_id=username)
            subscribe.delete()
        except Exception:
            pass

        return HttpResponseRedirect(f'/social_network/friends/{request.user.username}')


@login_required
def make_chat(request, username):
	if request.method == 'POST':
		Room().create_chat([username, request.user.username])
		return HttpResponseRedirect(f'/social_network/dialogs/{request.user.username}')
