from django.shortcuts import render

# Create your views here.
def services(request):
    context={'services':'active'}
    return render(request,'edu/services.html', context)
def skill(request):
    context={'skills':'active'}
    return render(request,'edu/skill.html',context)
