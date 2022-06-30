from django.shortcuts import render
from .models import stud_db_dest
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
 

    def Userregistration(request):
        if request.method=="POST":
            if request.POST.get("uname") and request.POST.get("usn") and request.POST.get("uid") and request.POST.get("pwd"):
                saverecord = Userreg()
                saverecord.uname = request.POST.get('uname')
                saverecord.uname = request.POST.get('usn')
                saverecord.uname = request.POST.get('usn')
                saverecord.uname = request.POST.get('pwd')
                saverecord.save()
                messages.success(request, "New User registration details has been saved successfully...!")
                return render(request,'registration.html')
        else:
                return render(request,'registration.html')