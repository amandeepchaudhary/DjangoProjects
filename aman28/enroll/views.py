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
                st = student()  # If we give this then there is a chance that it will submit twice so for preventing that to happen we need to give a seperate page on which we go after giving the details.
    else:
        st = student()

    return render(request, 'enroll/studetails.html', {'form':st})
