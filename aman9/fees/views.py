from django.shortcuts import render

# Create your views here.
def fees_Django(request):
    return render(request,'fees/feesone.html',{'tittle':'Django_Fees','corname':'Django','fees':'300','dur':'4 Months','seats':'490'})