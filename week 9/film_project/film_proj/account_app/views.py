from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, reverse
from .forms import SignUpForm
from django.views.generic import CreateView

# Create your views here.
class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'registration/sign_up.html'
    success_url = 'home'
    failed_message = "The User couldn't be added."

    def form_valid(self, form):
            super().form_valid(form)   

            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])

            if user:
                login(self.request, user)
                
            return redirect(reverse(self.get_success_url()))


def profile(request):
    return render(request, 'registration/profile.html')