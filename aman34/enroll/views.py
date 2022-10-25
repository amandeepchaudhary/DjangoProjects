from django.shortcuts import render
from enroll.forms import student


# Create your views here.


def studetails(request):
    if request.method == 'POST':
        st = student(request.POST)
        if st.is_valid():
            print('Form Validated')
            print('Name:', st.cleaned_data['name'])  # Key in forms
            print('Email:', st.cleaned_data['email'])  # Key in forms
            
    else:
        st = student()

    return render(request, 'enroll/studetails.html', {'form':st})
