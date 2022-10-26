from django import forms    
from django.core import validators


class student(forms.Form):
    error_css_class = 'error'  # Gives class name as 'error' for the <tr> == means for the row. So, with help of this we can apply css for that error in that perticular row error. which shows itself as dynamic in view page source after getting an error 
    required_css_class = 'required'  # Gives class name as 'required' for the <tr> == means for the row. So, with help of this we can apply css for that required in that perticular row required. which shows itself as dynamic in view page source after getting an submit without giving it a value 
    name = forms.CharField(error_messages = {'required':'Enter your name'})
    email = forms.EmailField(error_messages = {'required':'Enter your email'}, min_length=10, max_length=50)
    password = forms.CharField(widget = forms.PasswordInput(),error_messages = {'required':'Enter your password'}, min_length=8, max_length=20)