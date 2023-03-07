from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import Blog, Subscriber


def index(request, username):
	if not request.user.is_authenticated:
		return HttpResponseRedirect('/social_network')

	result_dict = make_content(request, username)
	return render(request, 'user.html', result_dict)



def make_content(request, username):

	global_user = User.objects.get(username=request.user.username)

	try:
		user = User.objects.get(username=username)
	except User.DoesNotExist:
		return HttpResponseRedirect(f'/social_network/user/{request.user.username}')

	blog = Blog.objects.filter(user_id=username).order_by('-date_time')

	obj = Subscriber()
	friends_count = obj.get_friends(username=username)[0].count()

	result_dict = {
		'is_my_page': True,
		'global_user': global_user,
		'user': user,
		'blog': blog,
		'friends_count': friends_count,
	}

	# If I am on another user's page:
	if username != request.user.username:
		result_dict['is_my_page'] = False

		# If we are friends, I can see his blog
		if Subscriber.objects.filter(user=request.user.username, subscriber=username) and Subscriber.objects.filter(user=username, subscriber=request.user.username):
			result_dict['is_my_friend'] = True

	return result_dict



def quit(request, username):

	if request.method == 'GET' and request.user.is_authenticated:
		logout(request)
		return HttpResponseRedirect('/social_network')
	


def delete_account(request, username):

	if request.method == 'POST' and request.user.is_authenticated:
		User.objects.get(username=request.user.username).delete()
		Subscriber.objects.filter(subscriber=request.user.username).delete()

	return HttpResponseRedirect('/social_network')




def create_record(request, username):

	if request.method == 'POST' and request.user.is_authenticated and request.user.username == username:
		if request.POST.get('my_textarea'):
			Blog.objects.create(user_id=username, content=request.POST.get('my_textarea'))

		return HttpResponseRedirect(f'/social_network/user/{username}')
	else:
		return HttpResponseRedirect('/social_network')




def change_record(request, username, id):

	if request.method == 'POST' and request.user.is_authenticated and request.user.username == username:
		if request.POST.get('my_textarea'):
			record = Blog.objects.get(user_id=username, id=id)
			record.content=request.POST.get('my_textarea')
			record.is_changed = True
			record.save()
		return HttpResponseRedirect(f'/social_network/user/{username}')
	else:
		return HttpResponseRedirect('/social_network')




def delete_record(request, username, id):

	if request.method == 'POST' and request.user.is_authenticated and request.user.username == username:
		try:
			record = Blog.objects.get(user_id=username, id=id)
			record.delete()
			return HttpResponseRedirect(f'/social_network/user/{username}')
		except Blog.DoesNotExist:
			pass
	else:
		return HttpResponseRedirect('/social_network')



def update_user_info(request, username):
	if request.method == 'POST' and request.user.is_authenticated:
		
		user = User.objects.get(username=request.user.username)
		user.first_name = str(request.POST.get('fname')).strip()
		user.last_name = str(request.POST.get('lname')).strip()
		user.email = request.POST.get('email')
		user.save()

		return HttpResponseRedirect(f'/social_network/user/{username}')
	else:
		return HttpResponseRedirect('/social_network')
