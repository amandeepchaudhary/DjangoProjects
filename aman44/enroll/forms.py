from django import forms
from enroll.models import Student

class stuform(forms.ModelForm):
    class Meta:
        model = Student
        # fields = ['name','email','password']
        # fields = '__all__'  # Used to get all the fields,and the order of the fields will be same as in the model.py  
        exclude = ['name']  # This will Exclude the name field in the form