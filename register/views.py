from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, LoginForm
from user.models import User, Blog, UserSettings


def user_login(request):
	if request.method == "POST":
		form = LoginForm(data=request.POST)

		if form.is_valid():
			return user_auth(request)
		else:
			messages.error(request, "Incorrect login or password")
	else:
		if request.user.is_authenticated:
			return redirect("user", request.user.username)

		form = LoginForm()
	return render(request, "login.html", {"loginform": form})


def user_register(request):
	if request.method == "POST":
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Account created successfully")
			create_first_post(request)
			return user_auth(request)
		else:
			messages.error(request, "Error")
	else:
		form = CustomUserCreationForm()
	return render(request, "register.html", {"registerform": form})


def user_auth(request):
	username = request.POST.get("username")
	password = request.POST.get("password")
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		return redirect("user", username)
	else:
		messages.error(request, "Incorrect login or password")
		return redirect("login")


def create_first_post(request):
	username = request.POST.get("username")
	first_name = request.POST.get("first_name")
	last_name = request.POST.get("last_name")
	Blog.objects.create(user_id=username, content=f"Hi, I'm {first_name} {last_name} and this is my first post!")
	UserSettings.objects.create(user_id=username)


def is_username_new(request, username):
	is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"

	if is_ajax and request.method == "GET":
		try:
			User.objects.get(username=username)
			return JsonResponse({"status": False})
		except User.DoesNotExist:
			return JsonResponse({"status": True})
	return redirect("login")
