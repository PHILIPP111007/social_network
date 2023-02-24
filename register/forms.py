from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
	first_name = forms.CharField(min_length=1, max_length=20)
	last_name = forms.CharField(min_length=1, max_length=20)
	username = forms.CharField(min_length=1, max_length=20, help_text='(придумайте уникальное имя)')
	email = forms.EmailField(max_length=254)
	password = forms.CharField(label='Password', min_length=8, widget=forms.PasswordInput(), help_text='(пароль должен содержать более 8 символов)')
	password2 = forms.CharField(label='Repeat password', min_length=8, widget=forms.PasswordInput())
	
	def clean(self):
		cleaned_data = super().clean()
		username = cleaned_data.get('username')
		password  = cleaned_data.get('password')
		password2  = cleaned_data.get('password2')

		if User.objects.filter(username=username):
			raise forms.ValidationError('Someone is already using your nickname')
		
		if password != password2:
			raise forms.ValidationError('Passwords don\'t match.')




class LoginForm(forms.Form):
	username = forms.CharField(min_length=1, max_length=20)
	password = forms.CharField(min_length=8, widget=forms.PasswordInput())

