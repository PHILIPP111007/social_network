from django.urls import path
from friends import views


urlpatterns = [
	path('', views.index, name='friends'),
	path('quit/', views.quit),
	path('add_friend/<str:username>/', views.add_friend),
	path('delete_friend/<str:username>/', views.delete_friend),
	path('delete_subscriber/<str:username>/', views.delete_subscriber),
	path('make_chat/<str:username>/', views.make_chat)
]