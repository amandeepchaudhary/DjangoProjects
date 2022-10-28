from django.shortcuts import render

# Create your views here.


def home(request, Check):
    return render(request, 'enroll/home.html', {'ch':Check})

# def details(request, my_id):
#     student = {'id': my_id , 'name':'aman'}
#     return render(request, 'enroll/students.html', student)

def details(request, my_id = 1):  # This default value appears if the given value in the url is not happens to work
    if my_id == 1:
        student = {'id': my_id , 'name':'Aman'}
    if my_id == 2:
        student = {'id': my_id , 'name':'Ishu'}
    if my_id == 3:
        student = {'id': my_id , 'name':'Sunita'}
    if my_id == 4:
        student = {'id': my_id , 'name':'Surender'}
    return render(request, 'enroll/students.html', student)


def subdetails(request, my_id, my_subid):
    if my_id == 1 and my_subid == 5:
        student = {'id': my_id , 'name':'Aman', 'info':'Sub'}
    if my_id == 2 and my_subid == 6:
        student = {'id': my_id , 'name':'Ishu', 'info':'Sub'}
    if my_id == 3 and my_subid == 7:
        student = {'id': my_id , 'name':'Sunita', 'info':'Sub'}
    if my_id == 4 and my_subid == 8:
        student = {'id': my_id , 'name':'Surender', 'info':'Sub'}
    return render(request, 'enroll/students.html', student)