from django.shortcuts import render
from django.http import HttpResponse
from .models import Department,Doctor,Booking
from .forms import BookingForms
#Create your views here
def index(request):
    #return httpresponse("Hello welcome")
    person={
        'name':'john',
        'age':30,
        'place':'Thrissur'
    }
    return render(request,"index.html",person)
def about(request):
    return render(request,"about.html",{'range':range(1,11)})
  #  return HttpResponse("About Us")
def show(request):
    number1={
        'num':[1,2,3,4,5,6,7,8,9,10]
    }
    return render(request,"show.html",number1)
def Departments(request):
    dic_dept={
        'dept':Department.objects.all()
    }
    return render(request,"Department.html",dic_dept)
def Doctors(request):
    dic_doc={
        'doc':Doctor.objects.all()
    }
    return render(request,"Doctor.html",dic_doc)
def bookings(request):
    if request.method=="POST":
        form=BookingForms(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=BookingForms()
    dic_form={
        'form':form
    }
    return render(request,"Booking.html",dic_form)