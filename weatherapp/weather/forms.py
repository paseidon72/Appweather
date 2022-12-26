from .models import City
from django.forms import ModelForm, TextInput

class CityForm(ModelForm):
    class Meta:
        madel = City
        fields = ['name']
        widgets = {'name': TextInput(attrs={
            'class': 'form-control',
            'nme': 'city',
            'id': 'city',
            'placeholder': 'Введите город'
        })}
