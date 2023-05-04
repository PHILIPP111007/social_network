from django.urls import path
from . import views


urlpatterns = [
	path("", views.dialogs, name="dialogs"),
	path('quit/', views.quit),
	path("remove_chat/<str:room_name>/", views.remove_chat),
	path("chat/<str:room_name>/", views.room),
	path('background_color_change/', views.background_color_change)
]
