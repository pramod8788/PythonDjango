from django.contrib import admin
from . models import course, follower, applyforcourse, message, chatroom

admin.site.register(course)
admin.site.register(follower)
admin.site.register(applyforcourse)
admin.site.register(message)
admin.site.register(chatroom)