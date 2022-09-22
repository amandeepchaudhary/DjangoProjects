from django.shortcuts import render

# Create your views here.

def learn_Django(request):
    return render(request,'courseone.html')

def learn_Python(request):
    return render(request,'coursetwo.html')