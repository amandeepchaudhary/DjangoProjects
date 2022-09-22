from django.shortcuts import render

# Create your views here.

def fees_Django(request):
    return render(request,'feesone.html')

def fees_Python(request):
    return render(request,'feestwo.html')