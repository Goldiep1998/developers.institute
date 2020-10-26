from django.db import models
from django.contrib.auth.models import User
from datetime import datetime   
# Create your models here.

class Thread(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=datetime.now)

class Comment(models.Model):
    text =  models.TextField()
    thread_id = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=datetime.now)