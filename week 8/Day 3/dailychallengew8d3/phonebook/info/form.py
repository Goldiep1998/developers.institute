from django import forms
from .models import Person

class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = "__all__"
        exclude = ['address', 'email']

    phone_number = forms.IntegerField(required=False)
    name = forms.CharField(required=False)

       
       