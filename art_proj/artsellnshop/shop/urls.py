from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('gallery', views.gallery, name='gallery'),
    path('image-info/<int:id>', views.image_info, name='image-info'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('about', views.about, name='about'),
    path('buy/<int:id>', views.buy, name='buy'),
    path('edit/<int:id>', views.edit, name='edit'),


]