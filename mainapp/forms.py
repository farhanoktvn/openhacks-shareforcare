from django import forms
from location_field.forms.plain import PlainLocationField

class PostForm(forms.Form):

    message = forms.CharField(widget=forms.TextInput(attrs={
        'type' : 'text',
        'class' : 'form-control',
        'maxlength' : '280',
        'required' : True,
        'placeholder' : 'I need/have ...',
        'label': 'Message',
    }))
    city = forms.CharField(widget=forms.TextInput(attrs={
        'type' : 'text',
        'class' : 'form-control',
        'maxlength' : '255',
        'required' : True,
        'placeholder' : 'Jakarta',
        'label': 'City',
    }))

class ReplyForm(forms.Form):

    message = forms.CharField(widget=forms.TextInput(attrs={
        'type' : 'text',
        'class' : 'form-control',
        'maxlength' : '280',
        'required' : True,
        'placeholder' : 'Hi there, I want to ...',
        'label': 'Message',
    }))
