from django.shortcuts import render

# Create your views here.
def todays(request):
    return render(request,'todays/content.html')