from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def fees_Django(request):
    students={'names':['aman','diksha','ishu','shivani']}                        #Dot Lookup
    return render(request,'fees/feesone.html',students)  #empty mai ",students must be removed"

def fees_Python(request):
    students={'stu1':{'name':'aman','roll_no':'21'},
              'stu2':{'name':'diksha','roll_no':'2132'},
              'stu3':{'name':'ishu','roll_no':'2143'},
              'stu4':{'name':'dharmo','roll_no':'2165'},}        #Nested For loop with Dot Lookup and forloop.parentloop variable of for loop for knowing the parent of the loop
    s={'stu':students}
    return render(request,'fees/feestwo.html',s)

def fees_DTL(request):
    student={'stu1':{'name':'aman','roll_no':'21'},
              'stu2':{'name':'diksha','roll_no':'2132'},
              'stu3':{'name':'ishu','roll_no':'2143'},
              'stu4':{'name':'dharmo','roll_no':'2165'},} 
    return render(request,'fees/feesthree.html',{'stu':student})