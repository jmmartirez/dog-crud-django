from django import forms
from . models import Dog


class DogForms(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ['name', 'color', 'breed']

    name = forms.CharField(max_length=10, required=False)
    color = forms.CharField(max_length=10, required=False)
    breed = forms.CharField(max_length=10, required=False)
