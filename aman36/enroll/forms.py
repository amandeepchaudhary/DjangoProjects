from django import forms    
from django.core import validators


class student(forms.Form):
    name = forms.CharField(error_messages = {'required':'Enter your name'})
    email = forms.EmailField(error_messages = {'required':'Enter your email'}, min_length=10, max_length=50)
    password = forms.CharField(widget = forms.PasswordInput(),error_messages = {'required':'Enter your password'}, min_length=8, max_length=20)