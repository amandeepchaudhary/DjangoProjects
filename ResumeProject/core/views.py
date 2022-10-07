from django.shortcuts import render

# Create your views here.
def home(request):
    context={'home':'active'}
    return render(request,'core/home.html',context)
    print(request)
def contact(request):
    context={'contact':'active'}
    return render(request,'core/contact.html',context)