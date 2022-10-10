from django.shortcuts import render

# Create your views here.
def stuhome(request):
    return render(request,'enroll/home.html')
def stuinfo(request):
    return render(request,'enroll/studetails.html')