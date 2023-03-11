from django.urls import path
from user import views


urlpatterns = [
	path('', views.index, name='user'),
	path('quit/', views.quit),
	path('delete_account/', views.delete_account),
	path('create_record/', views.create_record),
	path('change_record/<int:id>/', views.change_record),
	path('delete_record/<int:id>/', views.delete_record),
	path('update_user_info/', views.update_user_info),
	path('update_user_settings/', views.update_user_settings),
    path('add_friend/<str:username>/', views.add_friend),
	path('delete_friend/<str:username>/', views.delete_friend),
	path('delete_subscriber/<str:username>/', views.delete_subscriber)
]
