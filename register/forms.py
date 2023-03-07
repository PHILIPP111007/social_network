from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
	first_name = forms.CharField(min_length=1, max_length=20, strip=True)
	last_name = forms.CharField(min_length=1, max_length=20, strip=True)
	username = forms.CharField(min_length=1, max_length=20, strip=True, help_text='(create a unique name)')
	email = forms.EmailField(max_length=254)
	password = forms.CharField(label='Password', min_length=8, strip=True, widget=forms.PasswordInput(), help_text='(password must be more than 8 characters long)')
	password2 = forms.CharField(label='Repeat password', strip=True, min_length=8, widget=forms.PasswordInput())
	
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
