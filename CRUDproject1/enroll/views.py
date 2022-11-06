from django.shortcuts import render, HttpResponseRedirect
from enroll.forms import StudentRegistration
from enroll.models import User

# Create your views here.

# This will Add and Show
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)  # Used the form import
        if fm.is_valid():
            nm = fm.cleaned_data['name']  # Used the Model import
            em = fm.cleaned_data['email']  # Used the Model import
            pw = fm.cleaned_data['password']  # Used the Model import
            #Object of Model Class==
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud})

# This will Update/Edit
def update_edit(request, id):  # id k sath dynamic url kyuki specific data pr kaam krna h isliye
    if request.method == 'POST':
        ud = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance = ud)  #This is done for getting a form having all the details of the given id
        if fm.is_valid():
            fm.save()
    else:
        ud = User.objects.get(pk=id)
        fm = StudentRegistration(instance = ud)
    return render(request, 'enroll/update.html', {'form':fm})


# This will Delete

def delete_stu(request, id):
    if request.method == 'POST':
        dt = User.objects.get(pk=id)
        dt.delete()
        return HttpResponseRedirect('/')