from django import forms

class StudentRegistration(forms.Form):
    first_name = forms.CharField()  # the "_" is converted into " "
    email = forms.EmailField()  # Not showing in web page because humne sara code hi first_name ka kara h so we study loop
    phone = forms.IntegerField()
    key = forms.CharField(widget=forms.HiddenInput())  # Sirf agar yh kr denge toh page pe name of the field "Key:" dikhega kyuki for loop chal rha h toh isliye hum for loop m template m {% for fields in form.visible_fields %} likhenge

    # iss class ka object banega views.py mai