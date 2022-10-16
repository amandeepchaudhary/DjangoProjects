from django.shortcuts import render
from enroll.forms import StudentRegistration

# Create your views here.


def StuReg(request):
    sr = StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form': sr})