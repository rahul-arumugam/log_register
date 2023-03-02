from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Employees
from django.template import loader
from django.urls import reverse
from django.http import HttpResponseRedirect
  

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    emp=Employees.objects.all().values()
    template=loader.get_template('home.html')
    context={
        'emp':emp
    }
    return HttpResponse(template.render(context,request))
def add(request):
    if request.method =="POST":
        name=request.POST.get('name')
        rollno=request.POST.get('rollno')
        intime=request.POST.get('intime')
        outtime=request.POST.get('outtime')
        nodeno=request.POST.get('nodeno')

        emp=Employees(
            name=name,
            rollno=rollno,
            Intime=intime,
            Outtime=outtime,
            nodeno=nodeno
        )
        emp.save()
        return redirect('thankyou')
    return render(request,'home.html')
    
"""def addrecord(request):
    x=request.POST['Name']
    y=request.POST['rollno']
    z=request.POST['nodeno']
    new =Newapp(Name=x,rollno=y,nodeno=z)
    new.save()
    return HttpResponseRedirect(reverse('home'))"""



    
def SignupPage(request):

    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return redirect('err')
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')

        
    return render(request,'signup.html')
def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('error')



            

        
    return render(request,'login.html')
def error(request):
    return render(request,'error.html')
def err(request):
    return render(request,'err.html')
def thankyou(request):
    return render(request,'thankyou.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

