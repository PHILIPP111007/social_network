from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
	first_name = forms.CharField(required=True, strip=True)
	last_name = forms.CharField(required=True, strip=True)
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
	username = forms.CharField(min_length=1, max_length=20)
	password = forms.CharField(min_length=8, widget=forms.PasswordInput())
