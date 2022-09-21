from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def fees_Django(request):
    return HttpResponse('Fees=3000')