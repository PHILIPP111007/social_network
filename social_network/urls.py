from django.contrib import admin
from django.urls import path, include


urlpatterns = [
	path('admin/', admin.site.urls),
	# path('accounts/', include('django.contrib.auth.urls')),  # Add Django site authentication urls (for login, logout, password management)
	
	path('', include('register.urls'), name='home'),
	path('user/<str:username>/', include('user.urls')),
	path('friends/<str:username>/', include('friends.urls')),
	path('news/<str:username>/', include('news.urls')),
	path('dialogs/<str:username>/', include('chat.urls'))
]
