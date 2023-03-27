from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .models import Profile
# Create your views here.
def home(request):
    return render(request,'index.html')

def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        fname=request.POST.get('fname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')

        if User.objects.filter(username=username):
            messages.error(request,"Username Already taken")
            return render(request,'index.html')

        
        if User.objects.filter(email=email):
            messages.error(request,"Email Already taken")
            return render(request,'index.html')
            
        
        if pass1!=pass2:
            messages.error(request,"Password didn't match")
            return render(request,'index.html')
            
            

        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.save()
        messages.success(request,'Your Account is Successfully created')
        return redirect('/')



    return render(request,'authen/signup.html')


def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(username=username,password=pass1)

        if user is not None:
            auth_login(request,user)
            return redirect('/',{'name':username})
        else:
            messages.error(request,'Bad Credentials')
            return render(request,'index.html')
            
        
    return render(request,'authen/login.html')

def logout(request):
    auth_logout(request)
    messages.success(request,"Logged out successfully")
    return render(request,'index.html')


def addb(request):
    muser=request.user
    if request.method=='POST':
        balance=request.POST.get('balance')
        if Profile.objects.filter(user=muser):
            for prof in Profile.objects.filter(user=muser):
                prof.balance=int(balance)+int(prof.balance)
                messages.error(request,'Balance Added')
                prof.save()
        else:
            myprof=Profile.objects.create(user=muser)
            myprof.balance=balance
            messages.error(request,'Balance Added')
            myprof.save();
        return redirect('/')
    if Profile.objects.filter(user=muser):
        myprof=Profile.objects.get(user=muser)
        return render(request,'addbalance.html',{'muser':myprof.balance})
    else:
        return render(request,'addbalance.html',{'muser':0})
