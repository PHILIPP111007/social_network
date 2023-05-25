from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User
from user.models import Subscriber, UserSettings


@login_required
def index(request, username):
	if request.method == 'POST':
		find_users = find_user(request)
		result_dict = make_content(request, find_users=find_users)
		return render(request, 'friends.html', result_dict)
	else:
		result_dict = make_content(request)
		return render(request, 'friends.html', result_dict)


def make_content(request, find_users=None):
	user = User.objects.get(username=request.user.username)
	settings = UserSettings.objects.get(user_id=request.user.username)
	friends, subscriptions, subscribers = Subscriber.get_friends_subscriptions_subscribers(username=request.user.username)

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


@login_required
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
			pass
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
			pass
	return JsonResponse({'status': False})
