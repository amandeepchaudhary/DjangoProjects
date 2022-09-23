from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def fees_Django(request):
    return render(request,'fees/feesone.html')

def fees_Python(request):
    return render(request,'fees/feestwo.html')