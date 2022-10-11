from django.shortcuts import render
from enroll.models import students
# Create your views here.
def stuhome(request):
    return render(request,'enroll/home.html')

def stuinfo(request):
    stud = students.objects.all()   #all() = returns Query set
    print('myoutput',stud)
    return render(request,'enroll/studetails.html',{'stu':stud})
