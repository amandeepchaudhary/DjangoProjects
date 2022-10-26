from django.core import validators
from django import forms


class student(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    rpassword = forms.CharField(widget=forms.PasswordInput(), label='Password(again)')

    def clean(self):
        cleaned_data = super().clean()
        valpass = self.cleaned_data['password']
        valrpass = self.cleaned_data['rpassword']
        if valrpass!=valpass:
            raise forms.ValidationError('Password Does Not Match')