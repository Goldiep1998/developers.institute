from django.contrib import admin
from .models import User, Todo, Category

# Register your models here.

admin.site.register(User)
admin.site.register(Todo)
admin.site.register(Category)