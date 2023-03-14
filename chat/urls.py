from django.urls import path
from . import views


urlpatterns = [
	path("", views.dialogs, name="dialogs"),
	path('quit/', views.quit),
	path("chat/<str:room_name>/", views.room)
]
