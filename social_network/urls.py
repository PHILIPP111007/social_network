from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve


urlpatterns = [
	path("admin/", admin.site.urls),
	path("", include("register.urls")),
	path("user/<str:username>/", include("user.urls")),
	path("friends/<str:username>/", include("friends.urls")),
	path("news/<str:username>/", include("news.urls")),
	path("dialogs/<str:username>/", include("chat.urls"))
]
