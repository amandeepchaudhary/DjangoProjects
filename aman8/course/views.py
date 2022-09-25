from django.shortcuts import render

# Create your views here.
def learn_Django(request):
    return render(request,'course/courseone.html',{'tittle':'Django','seats':'49','duration':'5 Months'})