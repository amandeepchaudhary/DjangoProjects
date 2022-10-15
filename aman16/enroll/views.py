from django.shortcuts import render
from enroll.models import Student

# Create your views here.


def studetails(request):
    stuinfo = Student.objects.all()
    return render(request, 'enroll/studetails.html', {'stu': stuinfo})
