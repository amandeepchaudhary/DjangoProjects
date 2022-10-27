from django import forms    
from enroll.models import user


class  studentform(forms.ModelForm):
    name = forms.CharField(max_length=30, required=False)  # Validators in ModelForm same as the Form API and this is a high priority and after this it takes from here and continue further down
    class Meta:
        model = user  # if we add () then it is callable,if () not there then it is not callable
        fields = ['name', 'email', 'password']
        labels = {"name": "Enter Your Name", "email": "Enter Your Email", "password": "Enter the Password"}
        help_text = {"name": "Yha p apka naam ayega"}
        error_messages = {"name": {"required": "Please Enter your name here"}, "email": {"required": "Please Enter your Email here"}, "password": {"required": "Please Enter your Password here"}}
        widgets = {"password":forms.PasswordInput(attrs={"placeholder":"Yha password likhiye"}),
        "name": forms.TextInput(attrs={"class": "myclass", "placeholder":"Yha naam likhiye"}), "email": forms.EmailInput(attrs={"placeholder":"Yha email likho"})}
        