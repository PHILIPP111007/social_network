from django.urls import path
from register import views


urlpatterns = [
	path("", views.user_login),
    path("login/", views.user_login),
    path("register/", views.user_register)
]
