from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.username}'

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()   

    def __str__(self):
        return f'{self.name}'

class Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    has_been_done = models.BooleanField(default=False)
    date_completion = models.DateField()
    deadline_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='todos')

    def __str__(self):
        return f'{self.title}'



