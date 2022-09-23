from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def learn_Django(request):
    return render(request,'course/courseone.html')

def learn_Python(request):
    return render(request,'course/coursetwo.html')