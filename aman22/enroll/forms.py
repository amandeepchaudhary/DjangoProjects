from django import forms

class StudentRegistration(forms.Form):
    first_name = forms.CharField(initial="aman@aman.com", help_text="this is the help field - hum char field m likh rahe h uske constructor mai Aur sara code 'View Page Source' m bhi nhi dikh rha hoga")  # the "_" is converted into " "
    email = forms.EmailField()  # Not showing in web page because humne sara code hi first_name ka kara h so we study loop

    # iss class ka object banega views.py mai