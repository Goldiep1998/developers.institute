from django.urls import path
from . import views

urlpatterns = [
   path('thread', views.ThreadView.as_view(), name='thread'),


]