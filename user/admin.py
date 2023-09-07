from django.contrib import admin
from .models import User, Blog, Like, Comment, Subscriber

# Register your models here.

admin.site.register(User)
admin.site.register(Blog)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Subscriber)