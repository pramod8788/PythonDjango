from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id' ,'title', 'completed', 'updated')