from django.shortcuts import render
from .models import People

# Create your views here.

def people_list(request):
    people = People.objects.all().order_by('age')
    return render (request, 'people_list.html', {'people': people})

def person_info(request, id):
    person = People.objects.get(id=id)
    return render(request, 'info.html', {'person':person})