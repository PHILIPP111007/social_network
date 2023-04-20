from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Room, Message


@login_required
def dialogs(request, username):
	result_dict = make_content(request)
	chats = Room().find_all_chats(username=request.user.username)


	if chats:
		a = chats[0]
		if username == a.user_1:
			user_list = chats.values_list('user_2', flat=True)
		else:
			user_list = chats.values_list('user_1', flat=True)
		
		dialogs = []
		for i, j in zip(chats.values_list('room_name', flat=True), user_list):
			dialogs.append([i, j])
		
		result_dict['dialogs'] = dialogs
	
	return render(request, 'dialogs.html', result_dict)


@login_required
def room(request, username, room_name):
	if Room.objects.filter(room_name=room_name):
		result_dict = make_content(request)
		result_dict["room_name"] = room_name
		result_dict["user_name"] = username

		try:
			messages = Message.objects.filter(room_id=room_name).order_by('timestamp')
			if messages:
				result_dict["messages"] = messages
		except Exception:
			pass

		return render(request, "room.html", result_dict)
	else:
		return HttpResponseRedirect(f'/social_network/dialogs/{request.user.username}')


def make_content(request):
	global_user = User.objects.get(username=request.user.username)

	result_dict = {
		'global_user': global_user
	}
	return result_dict


def quit(request, username):
	logout(request)
	return HttpResponseRedirect('/social_network')
