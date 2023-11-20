from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from . models import *
from . models import logn
from . models import regs


# Create your views here.
def login(request):
    if request.method=="POST":

        user_name=request.POST['user_name']
        password=request.POST['password']

        obj=regs.objects.filter(user_name=user_name,password=password).exists()
        if obj==True:
            return redirect('/')
        else:
            return redirect('login')

    else:
        return render(request,'login.html')
        



def register(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        user_name=request.POST.get('user_name')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        email=request.POST.get('email')
        if password1==password2:
            obj=regs(user_name=user_name,password=password1,email=email,first_name=first_name,last_name=last_name)
            obj.save()
            print("user created")
        else:
            print("password not matched")
        return redirect('/')
    else:
        
        return render(request,'registration.html')


def logout(request):
    auth.logout(request)
    return redirect('/')