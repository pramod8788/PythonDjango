from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import SET_NULL

class course(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    course_name = models.CharField(max_length=100)
    course_description = models.TextField(null=True)
    course_isactive = models.BooleanField(default=True)
    course_created = models.DateTimeField(auto_now_add=True)
    course_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-course_updated', '-course_created']

    def __str__(self):
        return str(self.course_name)

class follower(models.Model):
    mentor = models.CharField(max_length=150)
    student = models.CharField(max_length=150)

class applyforcourse(models.Model):
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    course_id = models.ForeignKey(course, on_delete=SET_NULL, null=True)
    accepted = models.BooleanField(default=False)