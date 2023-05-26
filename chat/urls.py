from django.urls import path, re_path
from chat import views
from user import views as user_views


urlpatterns = [
	path("", views.dialogs, name="dialogs"),
	path("remove_chat/<str:room_name>/", views.remove_chat),
	path("chat/<str:room_name>/", views.room, name="chat"),
	path("background_color_change/", user_views.background_color_change),
	path("quit/", user_views.quit)
]
