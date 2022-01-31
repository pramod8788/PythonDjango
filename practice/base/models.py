from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class info(models.Model):
    info = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.info


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class file(models.Model):
    uploads = models.FileField(upload_to="Uploads")
    rating = models.IntegerField(default=0,
        validators=[
           MaxValueValidator(5),
           MinValueValidator(0)
        ]
    )
    like = models.CharField(choices=LIKE_CHOICES, max_length=10, null=True)

    def __str__(self):
        return f"File id: {self.id}"
