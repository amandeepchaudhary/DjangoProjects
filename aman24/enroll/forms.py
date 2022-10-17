from django import forms


class Student(forms.Form):
    name = forms.CharField(label='Your Name', label_suffix=' ', initial='Aman', disabled=True, required=False, help_text='Maximum 100 Characters')
    # label default is 'name' but i gave it 'Your Name', label_suffix default is ':' but i gave it ' ', initial default is blank for user but i gave it 'Aman' and i gave a value in views.py too in dictionary form which will run at runtime, disabled default is 'False' but i gave it 'True' and the label will got disabled and user doesn't able to change anything in it, required default is 'True' but i gave it 'False' and the user is not required to give a value for it, help_text is used to give a help text to the user we can also apply css to the help text in template