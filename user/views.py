from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Blog, Subscriber, UserSettings
from chat.models import Room


@login_required
def index(request, username):
	result_dict = make_content(request, username)
	return render(request, 'user.html', result_dict)


def make_content(request, username):

	global_user = User.objects.get(username=request.user.username)

	# If I am on other persons's page:
	if username != request.user.username:
		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			return HttpResponseRedirect(f'/user/{request.user.username}')
		is_my_page = False
	else:
		is_my_page = True
		user = global_user
	
	blog = Blog.objects.filter(user_id=username)
	friends_count = Subscriber().get_friends(username=username).count()
	settings = UserSettings.objects.get(user_id=request.user.username)

	result_dict = {
		'is_my_page': is_my_page,
		'global_user': global_user,
		'user': user,
		'friends_count': friends_count,
		'blog': blog,
		'settings': settings
	}

	if not is_my_page:
		user_1 = Subscriber.objects.filter(user=request.user.username, subscribe=username)
		user_2 = Subscriber.objects.filter(user=username, subscribe=request.user.username)
		# If we are friends, I can see his blog
		if user_1 and user_2:
			result_dict['is_my_friend'] = True
		elif user_1:
			result_dict['i_am_subscriber'] = True
		elif user_2:
			result_dict['he_is_subscriber'] = True

	return result_dict


def quit(request, username):
	if request.method == 'POST':
		logout(request)
	return HttpResponseRedirect('/')
	

@login_required
def delete_account(request, username):
	if request.method == 'POST':
		Room.objects.filter(user_1=request.user.username).delete()
		Room.objects.filter(user_2=request.user.username).delete()
		User.objects.get(username=request.user.username).delete()

	return HttpResponseRedirect('/')


@login_required
def create_record(request, username):
	if request.method == 'POST':
		if request.POST.get('my_textarea'):
			Blog.objects.create(user_id=request.user.username, content=request.POST.get('my_textarea'))

	return HttpResponseRedirect(f'/user/{request.user.username}')


@login_required
def change_record(request, username, id):
	if request.method == 'POST':
		if request.POST.get('my_textarea', ''):
			record = Blog.objects.get(user_id=request.user.username, id=id)
			record.content=request.POST.get('my_textarea')
			record.is_changed = True
			record.save(update_fields=['content', 'is_changed'])

	return HttpResponseRedirect(f'/user/{request.user.username}')


@login_required
def delete_record(request, username, id):
	if request.method == 'POST':
		try:
			record = Blog.objects.get(user_id=request.user.username, id=id)
			record.delete()
		except Blog.DoesNotExist:
			pass

	return HttpResponseRedirect(f'/user/{request.user.username}')


@login_required
def update_user_info(request, username):
	if request.method == 'POST':
		user = User.objects.get(username=request.user.username)
		user.first_name = str(request.POST.get('fname')).strip()
		user.last_name = str(request.POST.get('lname')).strip()
		user.email = request.POST.get('email')
		user.save(update_fields=['first_name', 'last_name', 'email'])

	return HttpResponseRedirect(f'/user/{username}')


@login_required
def update_user_settings(request, username):
	if request.method == 'POST':
		settings = UserSettings.objects.get(user_id=request.user.username)
		if 'low_power_mode' in request.POST:
			settings.low_power_mode = False
		else:
			settings.low_power_mode = True
		settings.save(update_fields=['low_power_mode'])

	return HttpResponseRedirect(f'/user/{username}')


@login_required
def add_friend(request, username):
	if request.method == 'POST':
		if not Subscriber.objects.filter(user=request.user.username, subscribe=username):
			subscribe = User.objects.get(username=username)
			Subscriber.objects.create(user=request.user, subscribe=subscribe)
            
	return HttpResponseRedirect(f'/user/{username}')


@login_required
def delete_friend(request, username):
    if request.method == 'POST':
        try:
            subscribe = Subscriber.objects.get(subscribe=username, user=request.user.username)
            subscribe.delete()
        except Exception:
            pass

    return HttpResponseRedirect(f'/user/{username}')


@login_required
def delete_subscriber(request, username):
    if request.method == 'POST':
        try:
            subscribe = Subscriber.objects.get(subscribe=request.user.username, user=username)
            subscribe.delete()
        except Exception:
            pass

    return HttpResponseRedirect(f'/user/{username}')


@login_required
def make_chat(request, username):
	if request.method == 'POST':
		try:
			if Subscriber.objects.get(user=request.user.username, subscribe=username) and Subscriber.objects.get(user=username, subscribe=request.user.username):
				room_name = Room().create_chat(request_user=request.user.username, friend=username)
				return HttpResponseRedirect(f'/dialogs/{username}/chat/{room_name}/')
		except Exception:
			pass
	
	return HttpResponseRedirect(f'/dialogs/{request.user.username}')
