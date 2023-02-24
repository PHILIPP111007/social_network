from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import RegisterForm, LoginForm
from user.models import MyUser, Blog




def index(request):

	result_dict = {}

	if request.method == 'POST':

		if request.POST.get('first_name'):
			form = RegisterForm(request.POST)
			if form.is_valid():
				create_data(form='RegisterForm', request=request)
				username = request.POST.get('username')
				return HttpResponseRedirect(f'/social_network/user/{username}')
			else:
				result_dict['registerform'] = form
				result_dict['loginform'] = LoginForm()

		else:
			form = LoginForm(request.POST)
			if form.is_valid():
				create_data(form='LoginForm', request=request)
				username = request.POST.get('username')
				return HttpResponseRedirect(f'/social_network/user/{username}')
			else:
				result_dict['loginform'] = form
				result_dict['registerform'] = RegisterForm()
	else:
		result_dict['registerform'] = RegisterForm()
		result_dict['loginform'] = LoginForm()
	

	return render(request, 'register.html', result_dict)








def create_data(form, request):

	if form == 'RegisterForm':
		username = request.POST.get('username')
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		email = request.POST.get('email')
		password = request.POST.get('password')

		User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
		MyUser.objects.create(username=username, first_name=first_name, last_name=last_name)
		Blog.objects.create(user_id=username, content=f'Привет! Я {first_name} {last_name} и это моя первая запись!')
	
	elif form == 'LoginForm':
		username = request.POST.get('username')
		password = request.POST.get('password')
	
	
	user_login(request, username, password)




def user_login(request, username, password):

	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
	else:
		result_dict = {}
		result_dict['registerform'] = RegisterForm()
		result_dict['loginform'] = LoginForm()
		return render(request, 'register.html', result_dict)




