from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='MEDIA_ROOT/images')
    status = models.CharField(max_length=20, default='for-sale')
    price = models.IntegerField()
    description = models.TextField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
