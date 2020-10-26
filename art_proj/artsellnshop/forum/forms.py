from django.contrib.auth.models import User
from .models import Thread, Comment
from django import forms


class ThreadForm(forms.ModelForm):
    class meta:
        model = Thread
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class meta:
        model = Comment
        fields = "__all__"

