from django.shortcuts import render, redirect
from .form import AddFilmForm, AddDirectorForm
from .models import *
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin



def home(request):
    director=Director.objects.all()
    film=Film.objects.all()
    return render(request, 'homepage.html', context={'director':director, 'film':film}) 

class AddFilm(LoginRequiredMixin, CreateView):
    model = Film
    form_class = AddFilmForm
    template_name = 'film/add_film.html'
    success_url = reverse_lazy('home')
    

class AddDirector(LoginRequiredMixin, CreateView):
    model = Director
    form_class = AddDirectorForm
    template_name = 'director/add_director.html'
    success_url = reverse_lazy('home')


def delete_film(request, id):
    film = Film.objects.get(id=id)
    film.delete_film()
    return redirect('home')


