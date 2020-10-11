from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique=True)
    phone_number = models.IntegerField()
    address = models.CharField(max_length = 200)


