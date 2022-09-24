from django.shortcuts import render

# Create your views here.
def learn_Django(request):
    return render(request,'course/info.html')