from django.urls import path
from . import views

urlpatterns = [
    path('', views.people_list, name= 'people-list'),
    path('<int:id>', views.person_info, name= 'person_info')

]