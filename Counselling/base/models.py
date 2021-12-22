from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields.related import ForeignKey

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
    status = models.BooleanField(default=True)

    def __str__(self):
        val = f"{self.student} following {self.mentor}"
        return str(val)

class applyforcourse(models.Model):
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    course_id = models.ForeignKey(course, on_delete=SET_NULL, null=True)
    status = models.BooleanField(default=False)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        val = f"{self.user} applied for {self.course_id}"
        return str(val)

class chatroom(models.Model):
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)

    def __str__(self):
        val = f"Chat room for {self.sender} and {self.receiver}"
        return str(val)

class message(models.Model):
    chatroom = ForeignKey(chatroom, on_delete=SET_NULL, null=True)
    user = models.CharField(max_length=100)
    message_body = models.CharField(max_length=1000)
    message_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-message_created']

    def __str__(self):
        val = f"{self.user} messaged in {self.chatroom}"
        return str(val)

