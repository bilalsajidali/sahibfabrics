from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import AddStock_form
from .forms import register_form
from .models import Thaans_model
from .models import User_model
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.decorators import login_required




def home(request):
    return render(request,"home.html")

def account(request):            # account means login
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if password=='':
            messages.error(request,"Password Invalid")
            return redirect('account')

        if User.objects.filter(username=username).exists():
            user=authenticate(username=username,password=password)
            login(request,user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/addstock')
        else:
            messages.error(request,"Invalid Password!")
    else:
        return render(request,"account.html")

def logout_page(request):
    logout(request)
    return redirect('account')


    return render(request,"account")   


def register(request):
    if request.method == 'POST':
        fm=register_form(request.POST)
        if fm.is_valid():
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            hpw=make_password(password)   # hashing password

            user1=User.objects.filter(username=username)
            user2=User.objects.filter(email=email)
            if user1.exists():
                messages.info(request, "Username already exists!")
                return redirect('/register')
            elif user2.exists():
                messages.info(request, "email already exists!")
                return redirect('/register')

            #user creation adding to users(auth)
            user=User.objects.create(username=username,email=email,password=hpw)
            user.save()
            messages.success(request, "Register Successfully.")
            fm=register_form()
       
        return redirect('/account')

    else:
        fm=register_form()
    
    
    return render(request,"register.html",{'form':fm})


@login_required(login_url='/account')
def AddStock(request): # add and show stock
    if request.method == 'POST':
        fm=AddStock_form(request.POST)
        if fm.is_valid():
            fm.save()
            fm=AddStock_form()
            return redirect('/addstock')

    else:
        fm=AddStock_form()
    
    all_Thaans=Thaans_model.objects.all()
    return render(request,"AddStock.html",{'form':fm,'SD':all_Thaans})  #SD means Thaans Data (data of all Thaans)

def delete_stock(request,id):    #delete Thaan from stock
    if request.method=='POST':
        pi=Thaans_model.objects.get(pk=id)
        pi.delete()
        return redirect('/addstock')


def update_stock(request,id): #update Thaans or edit Thaans data

    if request.method =='POST':
        pi=Thaans_model.objects.get(pk=id)
        fm=AddStock_form(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('/addstock')
    else:
        pi=Thaans_model.objects.get(pk=id)
        fm=AddStock_form(instance=pi)

    return render(request,"UpdateStock.html",{'form':fm})