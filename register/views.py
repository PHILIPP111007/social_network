from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import LoginForm, CustomUserCreationForm
from user.models import Blog


def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user_auth(request)
			username = request.POST.get('username')
			return HttpResponseRedirect(f'/social_network/user/{username}')
		else:
			messages.error(request, 'Incorrect login or password')
	else:
		form = LoginForm()
	return render(request, 'login.html', {'loginform': form})


def user_register(request):
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			user_auth(request)
			messages.success(request, 'Account created successfully')
				
			username = request.POST.get('username')
			first_name = request.POST.get('first_name')
			last_name = request.POST.get('last_name')
			Blog.objects.create(user_id=username, content=f'Hi, I\'m {first_name} {last_name} and this is my first post!')

			return HttpResponseRedirect(f'/social_network/user/{username}')
	else:
		form = CustomUserCreationForm()
	return render(request, 'register.html', {'registerform': form})


def user_auth(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
	else:
		return render(request, 'login.html', {'loginform': LoginForm()}) 
