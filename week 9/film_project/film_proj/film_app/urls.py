from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('addfilm/', views.AddFilm.as_view(), name = 'add_film'),
    path('adddirector/', views.AddDirector.as_view(), name = 'add_director'),
    path('delete_film/<int:id>', views.delete_film, name = 'delete_film')
]