from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignupForm(UserCreationForm):

    name = forms.CharField(widget=forms.TextInput(attrs={
        'type' : 'text',
        'class' : 'form-control',
        'maxlength' : '175',
        'required' : True,
        'placeholder' : 'John Doe',
        'label': ''
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'type' : 'email',
        'class' : 'form-control',
        'maxlength' : '175',
        'required' : False,
        'placeholder' : 'johndoe@example.com',
        'label': ''
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'type' : 'text',
        'class' : 'form-control',
        'maxlength' : '32',
        'required' : True,
        'placeholder' : 'johndoe',
        'label': ''
    }))
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'type' : 'password',
        'class' : 'form-control',
        'maxlength' : '64',
        'required' : True,
        'placeholder' : 'Password',
        'label': ''
    }))
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'type' : 'password',
        'class' : 'form-control',
        'maxlength' : '64',
        'required' : True,
        'placeholder' : 'Password',
        'label': ''
    }))

class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'type' : 'text',
        'class' : 'form-control',
        'maxlength' : '32',
        'required' : True,
        'placeholder' : 'johndoe',
        'label': ''
    }))

    password = forms.CharField(widget=forms.TextInput(attrs={
        'type' : 'password',
        'class' : 'form-control',
        'maxlength' : '64',
        'required' : True,
        'placeholder' : 'Password',
        'label': ''
    }))
