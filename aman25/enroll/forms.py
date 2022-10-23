from django import forms

class student(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'csssheet', 'id':'uniqueid'}))
    # we use the "widget = forms." for the things which is not available in "form." || .Textarea, .passwordinput, .hiddeninput, .checkboxinput, .fileinput, .textinput 
    # attr in widgets used for the changes in attributes of the widgets like adding a css and changing the id name in the field, Jo bhi attributes hum change krna chahte h unhe pakdo view page source aur attr me key ki tarh likh k krdo change.