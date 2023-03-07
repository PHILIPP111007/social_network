""" For future ideas

from django import forms
from django.contrib.auth.models import User


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(required=True, max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))

    first_name = forms.CharField(min_length=1, max_length=20)
    last_name = forms.CharField(min_length=1, max_length=20)

    email = forms.EmailField(required=True, max_length=254, widget=forms.TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
"""
