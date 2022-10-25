from django.core import validators
from django import forms


def starts_with_a(value):
    if value[0]!='a':
        raise forms.ValidationError("Name should start with 'a'")

def sign_not_allowed(value):
    signs = ['!','@','#','$','%','^','&','*','(',')','_','-','+','=']
    for sign in signs: 
        if sign in value:
            raise forms.ValidationError('Enter without signs')

class student(forms.Form):
    name = forms.CharField(validators=[starts_with_a, sign_not_allowed])
    email = forms.EmailField()