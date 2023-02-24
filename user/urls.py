from django.urls import path
from user import views


urlpatterns = [
	path('', views.index),
	path('quit/', views.quit),
	path('delete_account/', views.delete_account),
	path('create_record/', views.create_record),
	path('change_record/<int:id>/', views.change_record),
	path('delete_record/<int:id>/', views.delete_record)
]
