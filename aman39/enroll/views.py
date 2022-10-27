from django.shortcuts import render
from enroll.forms import studentform
from django.http import HttpResponseRedirect


# Create your views here.


def success(request):
    return render(request, 'enroll/success.html')

def sturegistration(request):
    if request.method == 'POST':
        st = studentform(request.POST)
        if st.is_valid():
            nm = st.cleaned_data['name']
            em = st.cleaned_data['email']
            ps = st.cleaned_data['password']
            print(nm)
            print(em)
            print(ps)
            return HttpResponseRedirect('/success/')
            
    else:        
        st = studentform()
    return render(request, 'enroll/registration.html', {'form':st})