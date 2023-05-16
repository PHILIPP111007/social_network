from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from .settings import STATICFILES_DIRS  # for debug = False


urlpatterns = [
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': STATICFILES_DIRS[0]}),
	path('admin/', admin.site.urls),
	path('', include('register.urls'), name='home'),
	path('user/<str:username>/', include('user.urls')),
	path('friends/<str:username>/', include('friends.urls')),
	path('news/<str:username>/', include('news.urls')),
	path('dialogs/<str:username>/', include('chat.urls'))
]
