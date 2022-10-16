from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone = forms.IntegerField()

    # iss class ka object banega views.py mai