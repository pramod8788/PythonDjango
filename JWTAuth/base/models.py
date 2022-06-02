from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_num = models.CharField(max_length=20)
    phone_num = models.BigIntegerField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id} {self.name} ({self.roll_num})" 