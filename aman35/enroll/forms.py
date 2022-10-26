from django import forms    
from django.core import validators


class student(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    rpassword = forms.CharField(label='Password(again)', widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        valpwd = cleaned_data['password']
        valrpwd = cleaned_data['rpassword']
        if len(valpwd) and len(valrpwd) < 8:
            raise forms.ValidationError('Password aleast having 8 Characters')
        if valpwd != valrpwd:
            raise forms.ValidationError('Password Does Not Match!!!')