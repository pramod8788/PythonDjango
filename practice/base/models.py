from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class info(models.Model):
    info = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.info


class file(models.Model):
    uploads = models.FileField(upload_to="Uploads")
    rating = models.IntegerField(default=0,
        validators=[
           MaxValueValidator(5),
           MinValueValidator(0)
        ]
    )

    def __str__(self):
        return f"File id: {self.id}"
