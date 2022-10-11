from django.shortcuts import render
from enroll.models import students
# Create your views here.


def stuhome(request):
    return render(request, 'enroll/home.html')


def stuinfo(request):
    stud = students.objects.all()   # all() = returns Query set
    # if we want the data for a single identity then we use get()
    stud = students.objects.get(pk=2)  # where pk is the private key of that identity
    print('myoutput', stud)
    return render(request, 'enroll/studetails.html', {'stu': stud})
