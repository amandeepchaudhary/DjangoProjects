from django.shortcuts import render
from enroll.forms import student

# Create your views here.


def studetails(request):
    if request.method == 'POST':
        st = student(request.POST)
        if st.is_valid():
                name = st.cleaned_data['name']
                email = st.cleaned_data['email']
                password = st.cleaned_data['password']
                print('Name:', name)
                print('Email:', email)
                print('Password:', password)
    else:
        st = student()

    return render(request, 'enroll/studetails.html', {'form':st})
