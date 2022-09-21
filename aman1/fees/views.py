from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def fees_Django(request):
    return HttpResponse('300')

def fees_Python(request):
    return HttpResponse('1300')

def fees_var(request):
    a='900'
    return HttpResponse(a)

def fees_math(request):
    a=400+40000
    return HttpResponse(a)

def fees_format(request):
    a='9000'
    return HttpResponse(f'The fees of all courses {a}')