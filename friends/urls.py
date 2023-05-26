from django.urls import path
from . import views
from user import views as user_views


urlpatterns = [
	path("", views.index, name="friends"),
	path("add_friend/<str:username>/", views.add_friend),
	path("delete_friend/<str:username>/", views.delete_friend),
	path("delete_subscriber/<str:username>/", views.delete_subscriber),
	path("make_chat/<str:username>/", user_views.make_chat),
	path("quit/", user_views.quit),
	path("background_color_change/", user_views.background_color_change)
]
