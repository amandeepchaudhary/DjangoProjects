from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def learn_Django(request):
    return HttpResponse('Hello Django')

def learn_Python(request):
    return HttpResponse('Hello Python')