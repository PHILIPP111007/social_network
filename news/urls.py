from django.urls import path
from news import views
from user import views as user_views


urlpatterns = [
	path('', views.index, name='news'),
	path('quit/', user_views.quit),
	path('background_color_change/', user_views.background_color_change)
]
