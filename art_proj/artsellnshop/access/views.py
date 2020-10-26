from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, reverse
from .forms import SignUpForm
from django.views.generic import CreateView, UpdateView
from .models import Profile




# Create your views here.
class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'registration/sign_up.html'
    failed_message = "User was not added. Please try again."
    success_url = 'profile_update'

    def form_valid(self, form):
        super().form_valid(form)   

        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])

        if user:
            login(self.request, user)
                    
        return redirect('profile_update', user.profile.id)
    
    
class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ["bio", "image"]
    success_url = 'profile'
    
def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'access/profile.html', {'profile': profile})
    