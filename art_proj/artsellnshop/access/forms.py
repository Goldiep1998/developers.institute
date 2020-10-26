from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password1", "password2", "email", "date_joined"]
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['date_joined'].widget.attrs['readonly'] = True
