from django.shortcuts import render

# Create your views here.
def students(request):
    return render(request,'enroll/students.html')