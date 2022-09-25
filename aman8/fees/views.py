from django.shortcuts import render

# Create your views here.
def fees_Django(request):
    return render(request,'fees/feesone.html',{'tittle':'Django Fees','fees':'3000'})