from django.urls import path
from . import views


urlpatterns = [
	path("", views.user_login),
    path("login/", views.user_login, name="login"),
    path("register/", views.user_register, name="register"),
    path("register/is_username_new/<str:username>", views.is_username_new)
]
