from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from user.models import Subscriber, UserSettings
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
	settings = UserSettings.objects.get(user_id=request.user.username)
	obj = Subscriber()
	friends, subscriptions, subscribers = obj.get_friends_subscriptions_subscribers(username=request.user.username)

	result_dict = {
		'user': user,
		'settings': settings,
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
	if request.method == 'GET':
		logout(request)
	return HttpResponseRedirect('/')


def find_user(request):
	username = request.POST.get('username')
	find_users = ''

	if username != '':
		find_users = User.objects.filter(username__icontains=username)
	else:
		result_str = 'User.objects'

		first_name = request.POST.get('first_name')
		if first_name != '':
			result_str += f'.filter(first_name__icontains="{first_name}")'

		last_name = request.POST.get('last_name')
		if last_name != '':
			result_str += f'.filter(last_name__icontains="{last_name}")'

		if result_str != 'User.objects':
			find_users = eval(result_str)

	if find_users:
		find_users = find_users.exclude(username=request.user.username)
		return find_users


@login_required
def add_friend(request, username):
	is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
	if is_ajax and request.method == 'POST':
		if not Subscriber.objects.filter(user=request.user.username, subscribe=username).count():
			subscribe = User.objects.get(username=username)
			Subscriber.objects.create(user=request.user, subscribe=subscribe)
				
			return JsonResponse({
				'status': True,
				'username': subscribe.username,
				'first_name': subscribe.first_name,
				'last_name': subscribe.last_name
			})

		return JsonResponse({'status': False})


@login_required
def delete_friend(request, username):
	is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
	if is_ajax and request.method == 'POST':
		try:
			subscribe = Subscriber.objects.get(subscribe=username, user=request.user.username)
			data = {
				'status': True,
				'username': subscribe.subscribe.username,
				'first_name': subscribe.subscribe.first_name,
				'last_name': subscribe.subscribe.last_name
			}
			subscribe.delete()
			return JsonResponse(data)
		except Subscriber.DoesNotExist:
			return JsonResponse({'status': False})


@login_required
def delete_subscriber(request, username):
	is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
	if is_ajax and request.method == 'POST':
		try:
			subscribe = Subscriber.objects.get(subscribe=request.user.username, user=username)
			subscribe.delete()
			return JsonResponse({'status': True})
		except Subscriber.DoesNotExist:
			return JsonResponse({'status': False})


@login_required
def make_chat(request, username):
	if request.method == 'POST':
		if Subscriber.objects.filter(user=username, subscribe=request.user.username).count():
			room_name = Room().create_chat(request_user=request.user.username, friend=username)
			return HttpResponseRedirect(f'/dialogs/{username}/chat/{room_name}/')

	return HttpResponseRedirect(f'/dialogs/{request.user.username}')


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
