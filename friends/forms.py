from django import forms


class FindUser(forms.Form):
	username = forms.CharField(required=False, max_length=20)
	first_name = forms.CharField(required=False, max_length=20)
	last_name = forms.CharField(required=False, max_length=20)
