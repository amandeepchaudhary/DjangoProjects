from django.shortcuts import render
from core.forms import VisitorInfo
from core.models import Visitor
# Create your views here.
def home(request):
    context={'home':'active'}
    return render(request,'core/home.html',context)
    print(request)
def contact(request):
    context={'contact':'active'}
    # csrf_protect
    if request.method == 'POST':
        visitor = VisitorInfo(request.POST)
        if visitor.is_valid():
             vm =visitor.cleaned_data['visitor_name'] #form ka data vm m gya
             em = visitor.cleaned_data['email']
             sub = visitor.cleaned_data['subject'] #form k sub m jo data aaya h agar voh clean h toh usse sub m dal do
             mes = visitor.cleaned_data['message']
             
             reg = Visitor(visitor_name = vm, email=em, subject=sub, message=mes) #form ka data vm m h aur vm ka data gya phir model m
             reg.save()
             visitor = VisitorInfo()
    else:
        visitor = VisitorInfo()
    return render(request,'core/contact.html',{'form': visitor})