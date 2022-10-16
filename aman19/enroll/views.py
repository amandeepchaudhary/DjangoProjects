from django.shortcuts import render
from enroll.forms import StudentRegistration

# Create your views here.


def StuReg(request):
    sr = StudentRegistration(auto_id=True, label_suffix=' ', initial={'name': 'aman', 'email': 'aman@aman.com'}) 
    # auto_id changes the id in html code we have three options True/False/ any string , In True the auto id will be the same as the name of the label , In False the auto id and label tag will be removed , And in any other String that is "aman" the id will change like aman_name  
    # label_suffix is the ":" symbol which is next to the english word that is present in the label
    # initial is used to give a initial value to the label in runtime, it is given in the form of dictionary where the key is the name of the label
    return render(request, 'enroll/userregistration.html', {'form': sr})