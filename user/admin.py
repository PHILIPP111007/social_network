from django.contrib import admin
from .models import MyUser, Blog, Subscriber

# Register your models here.


admin.site.register(MyUser)
admin.site.register(Blog)
admin.site.register(Subscriber)
