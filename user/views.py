from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import Blog, Subscriber, UserSettings
from chat.models import Room
from social_network.settings import POSTS_TO_DOWNLOAD


@login_required
def index(request, username):
	# If I am on other persons"s page:
	if username != request.user.username:
		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			return redirect("user", request.user.username)
		my_page = False
	else:
		my_page = True
		user = User.objects.get(username=request.user.username)

	global_user = User.objects.get(username=request.user.username)
	friends_count = Subscriber.get_friends(username=username).count()
	settings = UserSettings.objects.get(user_id=request.user.username)

	result_dict = {
		"is_my_page": my_page,
		"global_user": global_user,
		"user": user,
		"friends_count": friends_count,
		"settings": settings,
		"posts_to_download": POSTS_TO_DOWNLOAD
	}

	if not my_page:
		user_1 = Subscriber.objects.filter(user=request.user.username, subscribe=username)
		user_2 = Subscriber.objects.filter(user=username, subscribe=request.user.username)
		# If we are friends, I can see his blog
		if user_1 and user_2:
			result_dict["is_my_friend"] = True
		elif user_1:
			result_dict["i_am_subscriber"] = True
		elif user_2:
			result_dict["he_is_subscriber"] = True

	return render(request, "user.html", result_dict)



@login_required
def lazy_loader(request, username, posts_number):

	is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"
	if is_ajax and request.method == "GET":

		blog = Blog.objects.filter(user_id=username)[posts_number:posts_number + POSTS_TO_DOWNLOAD].values()

		result = [item for item in blog]

		for item in result:
			item["date_time"] = item["date_time"].strftime("%Y-%m-%d %H:%M")

		if result:
			return JsonResponse({
				"status": True,
				"blog": result
			})
	return JsonResponse({"status": False})


def quit(request, username):
	if request.method == "GET":
		logout(request)
	return redirect("login")
	

@login_required
def delete_account(request, username):
	if request.method == "POST":
		Room.objects.filter(user_1=request.user.username).delete()
		Room.objects.filter(user_2=request.user.username).delete()
		User.objects.get(username=request.user.username).delete()

	return redirect("login")


@login_required
def create_record(request, username):
	is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"
	if is_ajax and request.method == "POST":

		if request.body:
			body = request.body.decode("utf-8")

			new_record = Blog.objects.create(user_id=request.user.username, content=body)

			return JsonResponse({
				"status": True,
				"id": new_record.pk,
				"datetime": new_record.date_time.strftime("%Y-%m-%d %H:%M")
			})
	return JsonResponse({"status": False})


@login_required
def change_record(request, username, id):
	if request.method == "POST" and request.POST.get("my_textarea", ""):
		record = Blog.objects.get(user_id=request.user.username, id=id)
		record.content=request.POST.get("my_textarea")
		record.is_changed = True
		record.save(update_fields=["content", "is_changed"])

	return redirect("user", request.user.username)


@login_required
def delete_record(request, username, id):
	is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"
	if is_ajax and request.method == "POST":
		try:
			record = Blog.objects.get(user_id=request.user.username, id=id)
			record.delete()
			return JsonResponse({"status": True})
		except Blog.DoesNotExist:
			pass
	return JsonResponse({"status": False})


@login_required
def update_user_info(request, username):
	if request.method == "POST":
		user = User.objects.get(username=request.user.username)
		user.first_name = str(request.POST.get("fname")).strip()
		user.last_name = str(request.POST.get("lname")).strip()
		user.email = request.POST.get("email")
		user.save(update_fields=["first_name", "last_name", "email"])

	return redirect("user", username)


@login_required
def update_user_settings(request, username):
	if request.method == "POST":
		settings = UserSettings.objects.get(user_id=request.user.username)
		if "low_power_mode" in request.POST:
			settings.low_power_mode = False
		else:
			settings.low_power_mode = True
		settings.save(update_fields=["low_power_mode"])

	return redirect("user", username)


@login_required
def add_friend(request, username):
	if request.method == "POST":
		if not Subscriber.objects.filter(user=request.user.username, subscribe=username).count():
			subscribe = User.objects.get(username=username)
			Subscriber.objects.create(user=request.user, subscribe=subscribe)
	return redirect("user", username)


@login_required
def delete_friend(request, username):
	if request.method == "POST":
		try:
			subscribe = Subscriber.objects.get(subscribe=username, user=request.user.username)
			subscribe.delete()
		except Subscriber.DoesNotExist:
			pass
	return redirect("user", username)


@login_required
def delete_subscriber(request, username):
	if request.method == "POST":
		try:
			subscribe = Subscriber.objects.get(subscribe=request.user.username, user=username)
			subscribe.delete()
		except Subscriber.DoesNotExist:
			pass
	return redirect("user", username)


@login_required
def make_chat(request, username):
	if request.method == "POST":
		if Subscriber.objects.filter(user=username, subscribe=request.user.username).count():
			room_name = Room.create_chat(request_user=request.user.username, friend=username)
			return HttpResponseRedirect(f"/dialogs/{username}/chat/{room_name}/")
	return redirect("dialogs", request.user.username)


@login_required
def background_color_change(request, username):
	is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"

	if is_ajax and request.method == "POST" and request.body:

		color = not not int(request.body.decode("utf-8"))
		try:
			settings = UserSettings.objects.get(user_id=request.user.username)
			settings.theme = color
			settings.save(update_fields=["theme"])
			return JsonResponse({"status": True})
		except UserSettings.DoesNotExist:
			pass
	return JsonResponse({"status": False})
