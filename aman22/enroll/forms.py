from django import forms

class StudentRegistration(forms.Form):
    first_name = forms.CharField()  # the "_" is converted into " "
    email = forms.EmailField()  # Not showing in web page because humne sara code hi first_name ka kara h so we study loop
    phone = forms.IntegerField()
    # iss class ka object banega views.py mai