from django.shortcuts import render
from enroll.forms import student
from django.http import HttpResponseRedirect

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
            return HttpResponseRedirect('/success/')
            
    else:        
        st = student()
    return render(request, 'enroll/registration.html', {'form':st})