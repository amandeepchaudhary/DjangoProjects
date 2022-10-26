from django.shortcuts import render
from enroll.forms import student

# Create your views here.


def sturegistration(request):
    if request.method == 'POST':
        st = student(request.POST)
        if st.is_valid():
            print('Name:', st.cleaned_data['name'])
            print('Email:', st.cleaned_data['email'])
            print('Password:', st.cleaned_data['password'])
            print('Password(again):', st.cleaned_data['rpassword'])
    
    else:        
        st = student()
    return render(request, 'enroll/registration.html', {'form':st})