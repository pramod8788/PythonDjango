from django.contrib import admin
from . models import course, follower, applyforcourse, message

admin.site.register(course)
admin.site.register(follower)
admin.site.register(applyforcourse)
admin.site.register(message)