from django.shortcuts import render
from enroll.forms import studentform
from django.http import HttpResponseRedirect
from enroll.models import user


# Create your views here.


def success(request):
    return render(request, 'enroll/success.html')

def sturegistration(request):
    if request.method == 'POST':
        # Deleting a data using instance of primary key
        pi = user.objects.get(pk=1)  # primary key(pk)
        st = studentform(request.POST, instance=pk)  # Instance given as the primary key
        if st.is_valid():
            nm = st.cleaned_data['name']
            em = st.cleaned_data['email']
            ps = st.cleaned_data['password']
            print(nm)
            print(em)
            print(ps)
            # reg = user(name=nm, email=em, password=ps)
            # reg.save()
            # reg = user(id=1, name=nm, email=em, password=ps)  #for updateing the original data by giving the id or primary key
            # reg.save()
            # reg =user(id=1)
            # reg.delete()  # For deleting the existing data
            # pi.save()  # in instance we use the object of the user.object.get's
            return HttpResponseRedirect('/success/')
            
    else:        
        st = studentform()
    return render(request, 'enroll/registration.html', {'form':st})