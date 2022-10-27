from django import forms    
from django.core import validators


class student(forms.Form):
    name = forms.CharField(error_messages = {'required':'Enter your name'})
    email = forms.EmailField(error_messages = {'required':'Enter your email'})
    password = forms.CharField(widget = forms.PasswordInput(),error_messages = {'required':'Enter your password'})