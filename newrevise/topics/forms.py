from django import forms
from topics.models import dataModels

class childData(forms.ModelForm):
    class Meta:
        model = dataModels
        fields = ['name','email','password']
        widgets = {"password": forms.PasswordInput()}