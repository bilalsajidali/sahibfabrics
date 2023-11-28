from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import AddStock_form
from .models import Suits_model
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect

def home(request):
    return render(request,"home.html")

def account(request):
    return render(request,"login.html")   # account means login


def register(request):
    return render(request,"register.html")

def AddStock(request): # add and show stock
    if request.method == 'POST':
        fm=AddStock_form(request.POST)
        if fm.is_valid():
            fm.save()
            fm=AddStock_form()
            return redirect('/addstock')

    else:
        fm=AddStock_form()
    
    all_suits=Suits_model.objects.all()
    return render(request,"AddStock.html",{'form':fm,'SD':all_suits})  #SD means Suits Data (data of all suits)

def delete_stock(request,id):    #delete suit from stock
    if request.method=='POST':
        pi=Suits_model.objects.get(pk=id)
        pi.delete()
        return redirect('/addstock')