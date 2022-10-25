from django import forms


class student(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget= forms.PasswordInput())
    def clean_name(self):  # Field Validation
        signs = ['@','!','#','%','^','&','*','(',')','_','-','=','+']
        valname = self.cleaned_data['name']
        if len(valname)<4:
            raise forms.ValidationError('Enter more than or equal 4 char')
        for si in signs:  # we want to get a error message when user input the signs at the place of name 
            print(si)
            if si in valname:
                raise forms.ValidationError('Enter right name')
        return valname