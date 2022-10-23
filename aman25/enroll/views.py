from django.shortcuts import render
from enroll.forms import student

# Create your views here.


def details(request):
    stu = student()
    return render(request, 'enroll/studentdetails.html', {'form': stu})
