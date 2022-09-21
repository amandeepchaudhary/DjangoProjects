from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def learn_Django(request):
    return HttpResponse('Django urls in Application')