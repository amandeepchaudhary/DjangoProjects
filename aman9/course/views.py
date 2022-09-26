from django.shortcuts import render

# Create your views here.
def learn_Django(request):
    return render(request,'course/courseone.html',{'tittle':'Django','corname':'Django','dur':'4 Months','seats':'490'})