from django.shortcuts import render
from enroll.forms import StudentRegistration, TeacherRegistration
from enroll.models import User
# Create your views here.

def sturegistration(request):
    if request.method == 'POST':
        stu = StudentRegistration(request.POST)
        if stu.is_valid():
            # nm = stu.cleaned_data['student_name']
            stu.save()
            # reg = User(student_name=nm)
            # reg.save()
            stu = StudentRegistration()
    else:
        stu = StudentRegistration()
    return render(request, 'enroll/Studentregistration.html', {'form': stu})

def tecregistration(request):
    if request.method == 'POST':
        tec = TeacherRegistration(request.POST)        
        if tec.is_valid():
            tec.save()
            tec = TeacherRegistration()
    else:
        tec = TeacherRegistration()
    return render(request, 'enroll/Teacherregistration.html', {'form': tec})
