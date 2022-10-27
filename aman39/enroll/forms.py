from django import forms    
from enroll.models import user


class  studentform(forms.ModelForm):
    class Meta:
        model = user  # if we add () then it is callable,if () not there then it is not callable
        fields = ['name', 'email', 'password']