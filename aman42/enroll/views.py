from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'enroll/home.html')

def details(request, my_id):
    student = {'id': my_id}
    return render(request, 'enroll/students.html', student)