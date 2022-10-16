from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone = forms.IntegerField()
    first_name = forms.CharField()  # the "_" is converted into " "

    # iss class ka object banega views.py mai