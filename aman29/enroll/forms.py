from django import forms


class student(forms.Form):
    name = forms.CharField(min_length=3, max_length=25, strip= True,empty_value='This is Given Empty Value', error_messages={'required':'Enter your name!'})
    # Everything that is showing that the data is validated or not in the url is from the .is_valid in views.py  
    # Strip is True in deafult mode and it does not allow the data to have white spaces if we give it as False then it will allow the data to have the white spaces 

    roll = forms.IntegerField(max_value=20, min_value=1)
    
    price = forms.DecimalField(max_value=20, min_value=1, max_digits=4, decimal_places=2)

    rate = forms.FloatField(max_value=20, min_value=1)
    comment = forms.SlugField()
    email = forms.EmailField(max_length=20, min_length=1)
    website = forms.URLField(max_length=20, min_length=1)
    password = forms.CharField(max_length=20, min_length=1, widget= forms.PasswordInput())
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':2, 'cols':40}))
    feedback = forms.CharField(max_length=50, min_length=5, widget=forms.Textarea(attrs={'class':'somecss1 somecss2', 'id':'uniqueid', 'rows':2, 'cols':40}))
    notes = forms.CharField(widget=forms.Textarea(attrs={'rows':2, 'cols':40}))

    agree = forms.BooleanField(label='I Agree', label_suffix=' ', error_messages={'required':'Accept the Terms and Conditions for next step'})