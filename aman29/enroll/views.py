from django.shortcuts import render
from enroll.forms import student


# Create your views here.


def studetails(request):
    if request.method == 'POST':
        st = student(request.POST)
        if st.is_valid():
            print('Form Validated')
    else:
        st = student()

    return render(request, 'enroll/studetails.html', {'form':st})
