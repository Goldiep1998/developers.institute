from django.shortcuts import render
from .models import Person
from .form import PersonForm

# Create your views here.

def search_person(request):
    if request.method == 'GET':
        return render(request, 'search_person.html', context={'search_form': PersonForm()})
    if request.method == "POST":
        search_form = PersonForm(request.POST)
        if search_form.is_valid():
            s_form = search_form.save(commit=False)

            if s_form.name:
                if Person.objects.filter(name=s_form.name):
                    info = Person.objects.filter(name=s_form.name)
                else:
                    info = 'contact does not exist'
            elif s_form.phone_number:
                if Person.objects.filter(phone_number=s_form.phone_number):
                    info = Person.objects.filter(phone_number=s_form.phone_number) 
                else:
                    info = 'contact does not exist'
            else:
                info = 'type error'

            return render(request, 'outcome.html', context={'info': info})



    