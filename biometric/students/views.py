from django.shortcuts import render
from .models import stud_db_dest
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.

def Indexpage(request):
    return render(request, 'Index.html')

def Userreg(request):
    if request.method=="POST":
        Username=request.POST['uname']
        usn=request.POST['usn']
        uid=request.POST['uid']
        Pwd=request.POST['pwd']
        stud_db_dest(name=Username,cmritUSN=usn,UniqID=uid,Pwd=Pwd).save()
        messages.success(request,'The new User '+request.POST['Username']+" is saved Successfully...!")
        return render(request,'registration.html')
    else:
        return render(request,'registration.html')

def loginpage(request):
    if request.method=="POST":