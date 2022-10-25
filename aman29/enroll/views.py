from django.shortcuts import render
from enroll.forms import student


# Create your views here.


def studetails(request):
    if request.method == 'POST':
        st = student(request.POST)
        if st.is_valid():
            print('Form Validated')
            print('Name:', st.cleaned_data['name'])  # Key in forms
            print('Roll:', st.cleaned_data['roll'])  # Key in forms
            print('Price:', st.cleaned_data['price'])  # Key in forms
            print('Rate:', st.cleaned_data['rate'])  # Key in forms
            print('Comment:', st.cleaned_data['comment'])  # Key in forms
            print('Email:', st.cleaned_data['email'])  # Key in forms
            print('Website:', st.cleaned_data['website'])  # Key in forms
            print('Password:', st.cleaned_data['password'])  # Key in forms
            print('Description:', st.cleaned_data['description'])  # Key in forms
            print('Feedback:', st.cleaned_data['feedback'])  # Key in forms
            print('Notes:', st.cleaned_data['notes'])  # Key in forms

            print('Agree:', st.cleaned_data['agree'])  # Key in forms
    else:
        st = student()

    return render(request, 'enroll/studetails.html', {'form':st})
