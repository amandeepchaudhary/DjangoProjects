from django.shortcuts import render
from enroll.forms import stuform

# Create your views here.

def stureg(request):
    st = stuform()
    return render(request, 'enroll/sturegistration.html', {'form':st})