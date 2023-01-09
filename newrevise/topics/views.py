from django.shortcuts import render
from topics.models import dataModels
from topics.forms import childData

# Create your views here.

def newone(request):
    if request.method == "POST":
        data = childData(request.POST)
        if data.is_valid():
            data.save()
            data = childData()

    else:
        data = childData()

    return render(request, 'topics/home.html', {'form': data})