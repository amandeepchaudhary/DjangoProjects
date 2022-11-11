from django import forms
from enroll.models import User 


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['student_name', 'email', 'password']
        widgets = {"password": forms.PasswordInput()}

class TeacherRegistration(StudentRegistration):
    class Meta(StudentRegistration.Meta):  # model gets in child automatically by this
        fields = ['teacher_name', 'email', 'password']
        
