"""social_network URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Add Django site authentication urls (for login, logout, password management)
    
    path('social_network/', include('register.urls')),
    path('social_network/auth/', include('register.urls')),
    path('social_network/user/<str:username>/', include('user.urls')),
    path('social_network/friends/<str:username>/', include('friends.urls')),
    path('social_network/news/<str:username>/', include('news.urls')),
]
