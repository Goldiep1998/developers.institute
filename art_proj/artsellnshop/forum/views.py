from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Thread, Comment
# Create your views here.

class ThreadView(ListView):
    model = Thread
    template = 'threads_list.html'