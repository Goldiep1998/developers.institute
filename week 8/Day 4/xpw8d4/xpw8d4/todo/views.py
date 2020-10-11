from django.shortcuts import render, redirect
from .models import User, Todo, Category
from .forms import TodoForm, RegisterForm, UserForm
from django.contrib import messages

# Create your views here.

def user(request):
    if request.method == "GET":
        return render(request, "user.html", context={'user_form': UserForm()})

    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            u_form = user_form.save(commit=False)
            if User.objects.filter(username= u_form.username, password= u_form.password):
                user = User.objects.get(username= u_form.username, password= u_form.password)
                return redirect ('home', id=user.id)
            else:
                return redirect ('register')
        else:
            print("doesn't work")


def register(request):
    if request.method == "GET":
        return render(request, "register.html", context={'register_form': RegisterForm()})
    

    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            form = register_form.save()
            return redirect ('login')
        else:
            messages.error(request, 'Please correct the errors below.')
            return render(request, 'register.html', context={'register_form': RegisterForm()})

def home(request, id):
    user = User.objects.get(id=id)
    return render(request, 'home.html', {'user':user})
            


def todo(request, id):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            new_todo = form.save(commit=False)
            print(form)
            user = User.objects.get(id=id)
            new_todo.user = user
            new_todo.save()
            messages.success(request, 'Todo successfully added.')
            return redirect('todo', id=id)
            
    if request.method == "GET":
        return render(request, 'todo.html', {'form':TodoForm()})

def display_todos(request, id):
    lst = Todo.objects.filter(user__id=id)
    return render(request, 'display_todos.html', {'lst': lst, 'id': id})
    

