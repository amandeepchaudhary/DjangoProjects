from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse(f'Home Page Available Urls=learndj,learnpy,learnvar,learnm,learnf,feesdj,feespy,feesvar,feesm,feesf')

def learn_Django(request):
    return HttpResponse('<h1>Hello Django</h1>')

def learn_Python(request):
    return HttpResponse('<h2>Course:Python \n Fees:300</h3>')

def learn_var(request):
    a='<h1>Hello Variable</h1>'
    return HttpResponse(a)

def learn_math(request):
    a=20+23
    return HttpResponse(a)

def learn_format(request):
    a='Aman'
    return HttpResponse(f'Hello, How are you {a}')



