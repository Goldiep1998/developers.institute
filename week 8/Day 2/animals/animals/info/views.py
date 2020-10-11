from django.shortcuts import render
from .models import Animal, Family

# Create your views here.

def animals(request):
    animals = Animal.objects.all()
    return render(request, 'animals.html', {'animals': animals})
    

def familyinfo(request, id):
    animals = Animal.objects.filter(family_id = id) 

    return render(request, 'animal_families.html', {'animals': animals})
    
def animalinfo(request, id):
    animal = Animal.objects.get(id=id)

    return render(request, 'animal_info.html', {"animal": animal})    
 
