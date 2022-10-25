from django.shortcuts import render
from enroll.forms import Student

# Create your views here.


def stureg(request):
    if request.method == 'POST':
        st = Student(request.POST)  # This value will execute at runtime so it will overwrite the values given in forms.py
        if st.is_valid():
            print('Form Validated')
            print(st)
            print('ye post se ayya hai')
            print(st.cleaned_data)
            name = st.cleaned_data['name']
            email = st.cleaned_data['email']
            password = st.cleaned_data['password']
            print('Name:', name)
            print('Email:', email)
            print('Password:', password)
    
    else:
        st = Student()
        print('ye get se ayya hai')

    return render(request, 'enroll/userregistration.html', {'form': st})