from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from . import models
from accounts.models import Profile
from django.contrib import messages
import datetime
# Create your views here.

def sell(request):
    if request.user.is_authenticated:
        if request.method=='POST' and request.FILES['images']:
            name=request.POST.get('name')
            price=request.POST.get('price')
            category=request.POST.get('cat')
            lastd=request.POST.get('lastd')
            cur_date=datetime.datetime.now().strftime ("%Y-%m-%d")
            image=request.FILES['images']
            print(image)
            if cur_date>lastd:
                messages.error(request,'Cannot Give previous Dates')
                return render(request,'products/sell.html')
            else:
                muser=request.user
                prods=models.Products.objects.create(user=muser,name=name,price=price,category=category,last_date=lastd,prod_image=image)
                prods.save()
                return redirect('/')
        return render(request,'products/sell.html')
    else:
        return redirect('/')

def bid(request):
    if request.user.is_authenticated:
        prod=models.Products.objects.all()
        return render(request,'products/bid.html',{'prods':prod})
    return redirect('/')

def products(request,pk):
    if request.user.is_authenticated:
        prod=models.Products.objects.get(id=pk)
        cur_date=datetime.datetime.now().strftime ("%Y-%m-%d")
        check=True
        print(str(prod.last_date))
        if(str(prod.last_date)<cur_date):
            muser=prod.user
            prof=Profile.objects.get(user=muser)
            print(prof.balance)
            if prod.is_active:
                prof.balance=int(prof.balance)+int(prod.price)-1000
                prod.is_active=False
                prod.save()
                prof.save()
            check=False
        return render(request,'products/prod.html',{'prods':prod,'check':check})
    return redirect('/')


def bids(request,pk):
    if request.user.is_authenticated:
        prod=models.Products.objects.get(id=pk)
        prof=Profile.objects.filter(user=request.user)
        for p in prof:
            if int(p.balance)<int(prod.price):
                messages.error(request,'Low Balance')
                return redirect('/')
            else:
                if prod.latest_bid is not None:
                    lastuser=prod.latest_bid
                    userprof=User.objects.get(username=lastuser)
                    users=Profile.objects.get(user=userprof)
                    print(users.balance)
                    users.balance=int(users.balance)+int(prod.price)-1000
                    print(users.balance)
                    users.save()
                    prod.latest_bid=request.user.username
                else:
                    prod.latest_bid=request.user.username
                p.balance=int(p.balance)-int(prod.price)
                prod.price=int(prod.price)+int(1000)
                messages.success(request,'Bid SuccessFully')
                prod.save()
                p.save()
        return redirect('/')
    return redirect('/')

