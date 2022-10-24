from django.shortcuts import render
from enroll.forms import Student

# Create your views here.


def stureg(request):
    st = Student()  # This value will execute at runtime so it will overwrite the values given in forms.py
    return render(request, 'enroll/userregistration.html', {'form': st})