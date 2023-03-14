from django.contrib import admin
from django.urls import path, include


urlpatterns = [
	path('admin/', admin.site.urls),
	path('accounts/', include('django.contrib.auth.urls')),  # Add Django site authentication urls (for login, logout, password management)
	
	path('social_network/', include('register.urls'), name='home'),
	path('social_network/user/<str:username>/', include('user.urls')),
	path('social_network/friends/<str:username>/', include('friends.urls')),
	path('social_network/news/<str:username>/', include('news.urls')),
	path('social_network/dialogs/<str:username>/', include('chat.urls'))
]
