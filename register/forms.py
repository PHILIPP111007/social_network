from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class CustomUserCreationForm(UserCreationForm):

	class Meta:
		model = User

		fields = ("username", "first_name", "last_name", "password1", "password2")

		labels = {
            "username": "",
            "first_name": "",
            "last_name": ""
		}

		widgets = {
			"username": forms.TextInput(attrs={"placeholder": "username"}),
		 	"first_name": forms.TextInput(attrs={"placeholder": "first name"}),
			"last_name": forms.TextInput(attrs={"placeholder": "last name"})
		}
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.fields["username"].help_text = None

		self.fields["password1"].label = ""
		self.fields["password1"].help_text = "Your password must contain at least 8 characters"
		self.fields["password1"].widget = forms.PasswordInput(attrs={"placeholder": "password"})

		self.fields["password2"].label = ""
		self.fields["password2"].help_text = None
		self.fields["password2"].widget = forms.PasswordInput(attrs={"placeholder": "confirm password"})
	

class LoginForm(AuthenticationForm):
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.fields["username"].label = ""
		self.fields["username"].widget = forms.TextInput(attrs={"placeholder": "username"})

		self.fields["password"].label = ""
		self.fields["password"].widget = forms.PasswordInput(attrs={"placeholder": "password"})
