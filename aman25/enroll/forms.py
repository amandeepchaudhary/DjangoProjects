from django import forms

class student(forms.Form):
    name = forms.CharField(widget=forms.EmailInput())