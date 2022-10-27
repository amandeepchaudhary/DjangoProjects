from django.shortcuts import render
from enroll.forms import student
from django.http import HttpResponseRedirect
from enroll.models import user


# Create your views here.


def success(request):
    return render(request, 'enroll/success.html')

def sturegistration(request):
    if request.method == 'POST':
        st = student(request.POST)
        if st.is_valid():
            nm = st.cleaned_data['name']
            em = st.cleaned_data['email']
            ps = st.cleaned_data['password']
            reg = user(name=nm, email=em, password=ps)
            # reg = user(id=1, name=nm, email=em, password=ps) now it will update the details of the id=1
            reg.save()
            reg = user(id=1)  # The user id=1 will be deleted bcoz of
            reg.delete()    # <<<<<this operation
            return HttpResponseRedirect('/success/')
            
    else:        
        st = student()
    return render(request, 'enroll/registration.html', {'form':st})