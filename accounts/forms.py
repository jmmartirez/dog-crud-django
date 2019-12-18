from django import forms
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField(max_length=10, widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField(max_length=10, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=10, widget=forms.PasswordInput)


    def clean_username(self):
        try:
            user = User.objects.get(username=self.cleaned_data['username'])
        except User.DoesNotExist: 
            return self.cleaned_data['username']

        raise forms.ValidationError('Username already exists')


    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        if cleaned_data['password'] != cleaned_data['password2']:
            raise forms.ValidationError('Password doesn\'t match')

        return cleaned_data
