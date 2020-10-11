from django.urls import path
from . import views

urlpatterns = [
    path("", views.user, name='login'),
    path('todo/<int:id>/', views.todo, name='todo'),
    path('register/', views.register, name='register'),
    path('home/<int:id>/', views.home, name='home'),
    path('display_todos/<int:id>/', views.display_todos, name='display_todos')
]