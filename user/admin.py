from django.contrib import admin
from .models import Blog, Subscriber, UserSettings

# Register your models here.

admin.site.register(Blog)
admin.site.register(Subscriber)
admin.site.register(UserSettings)
