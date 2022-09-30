from django.shortcuts import render

# Create your views here.
def learn_course(request):
    return render(request,'course/courseone.html',{'d':'Django Course'})

def learn_python(request):
    return render(request,'course/coursepython.html',{'cn':'Pyhton','du':'4 Months','fs':'4000'})

def learn_django(request):
    return render(request,'course/coursedjango.html',{'cn':'Django','du':'5 Months','fs':'5000'})

def learn_javascript(request):
    return render(request,'course/coursejavascript.html',{'cn':'JavaScript','du':'2 Months','fs':'3000'})
