from django.urls import path
from . import views

urlpatterns = [
    path('', views.animals, name='animals'),
    path('family/<int:id>', views.familyinfo, name='family-info'),
    path('animals/<int:id>', views.animalinfo, name='info')

]