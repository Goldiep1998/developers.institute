from django import forms
from .models import Director, Film

class AddFilmForm(forms.ModelForm):
    class Meta:        
        model = Film
        fields = "__all__"
        widgets = { 'title' : forms.TextInput(attrs = {'placeholder': 'Enter Movie Title', 'class': 'form-control'}),
            'release_date' : forms.TextInput(attrs = {'placeholder': 'YYYY/MM/DD', 'class': 'form-control'}),
            'created_in_country' : forms.RadioSelect(),
            'available_in_countries' : forms.CheckboxSelectMultiple(),
            'category' : forms.CheckboxSelectMultiple(),
            'director' : forms.CheckboxSelectMultiple()
            }


class AddDirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = "__all__"
        widgets = { 'first_name' : forms.TextInput(attrs = {'placeholder': "Director's first name", 'class': 'form-control'}),
            'last_name' : forms.TextInput(attrs = {'placeholder': "Director's last name", 'class': 'form-control'})}

        

