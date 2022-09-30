from django.shortcuts import render

# Create your views here.
def contents(request):
    return render(request,'core/content.html')
def home(request):
    return render(request,'core/home.html')