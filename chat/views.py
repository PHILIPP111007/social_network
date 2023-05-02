from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from user.models import UserSettings
from .models import Room, Message


@login_required
def dialogs(request, username):
	result_dict = make_content(request)
	rooms = Room.objects.filter(room_name__contains=request.user.username)

	if rooms:
		dialogs = []
		for item in rooms:
			if request.user.username == item.delete_user_1 or request.user.username == item.delete_user_2:
				continue
			elif request.user.username == item.user_1:
				dialogs.append(
					(
						item.room_name,
						User.objects.get(username=item.user_2)
					)
				)
			elif request.user.username == item.user_2:
				dialogs.append(
					(
						item.room_name,
						User.objects.get(username=item.user_1)
					)
				)

		result_dict['dialogs'] = dialogs
	
	return render(request, 'dialogs.html', result_dict)


@login_required
def room(request, username, room_name):
	if Room.objects.filter(room_name=room_name):
		result_dict = make_content(request)
		result_dict['low_power_mode'] = UserSettings.objects.get(user=request.user.username).low_power_mode
		result_dict["room_name"] = room_name
		result_dict["friend"] = User.objects.get(username=username)

		messages = Message.objects.filter(room_name_id=room_name)
		if messages:
			result_dict["messages"] = messages

		return render(request, "room.html", result_dict)
	else:
		return HttpResponseRedirect(f'/dialogs/{request.user.username}')


def make_content(request):
	global_user = User.objects.get(username=request.user.username)

	result_dict = {
		'global_user': global_user
	}
	return result_dict


@login_required
def remove_chat(request, username, room_name):
	if request.method == 'POST':
		room = Room.objects.get(room_name=room_name)

		if room.user_1 == request.user.username:
			room.delete_user_1 = request.user.username
		elif room.user_2 == request.user.username:
			room.delete_user_2 = request.user.username
		room.save(update_fields=['delete_user_1', 'delete_user_2'])

		if room.delete_user_1 != '0' and room.delete_user_2 != '0':
			room.delete()

	return HttpResponseRedirect(f'/dialogs/{request.user.username}')


def quit(request, username):
	if request.method == 'GET':
		logout(request)
	return HttpResponseRedirect('/')
