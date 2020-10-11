from django import forms
from .models import Todo, User, Category


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class RegisterForm(forms.ModelForm):
    password = forms.CharField()
    class Meta:
        model = User
        fields = '__all__'


class TodoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        self.fields['user'].required = False
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })


    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all()) 

    class Meta:
        model = Todo
        fields = "__all__" 


    

