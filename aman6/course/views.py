from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
#two types of declaration - django=direct,,python=variable(indirect)

def learn_Django(request):
    d=datetime.now()

    Django_details={'nm':'django','du':'4 Months','st':'10 seats','av':'Online and Offline','tn':'Aman','dt':d}
    return render(request,'course/courseone.html',Django_details)

def learn_Python(request):
    name='Python'
    duration='2 Months'
    seats='40'
    Python_details={'nm':name,'du':duration,'st':seats}
    return render(request,'course/coursetwo.html',Python_details)