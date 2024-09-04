from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import merch,catgory
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import LoginForm
from . import views
from django.views.generic import CreateView
from django.urls import path
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import signup_form,updateuser_form,updatepasswordform
from django.contrib.auth import views as django_auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic

#from webSettings.mixins import SuperuserRequiredMixin

#from .models import User
from .forms import *


def home_page(request):
    all_merch=merch.objects.all()
     
    return render(request,"pages/home.html",{'merch':all_merch})
def about_page(request):
    return render(request,"pages/about.html")
def login_page(request):
     context = {}
     if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now log in')
            return redirect('pages:home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('pages:login')
     elif request.method == "GET":
        context['form'] = LoginForm()
     return render(request, 'pages/login.html', context)


@login_required(login_url='pages:login')

def logout_page(request):
    logout(request)
    messages.success(request,"you are now logout")
    return render(request,"pages/home.html")

def signup_page(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            User=form.save()
            messages.success(request,"you are new user")
            return render(request,'pages/login.html')
    else:

        form=UserCreationForm()    
    context={'form':form}
    return render(request,'pages/signup.html',context)
def catgory_page(request,cat):
    cat=cat.replace("-"," ")
    try:
        catgory=catgory.objects.get(name=cat)
        merch=merch.objects.filter(catgory=catgory)
        return render(request,'catgory.html',{'merch':merch,'catgory':catgory})
    
    except:
        messages.success(request,("you are now in home"))
        return redirect('pages:home')



        
def cart_page(request):
    return render(request,"pages/cart1.html")
#def carts_add(request):
 #   pass
#def carts_delete(request):
    pass
#def carts_update(request):
 #   pass
def merch_page(request,pk):
    product=merch.objects.get(id=pk)
     
    return render(request,"pages/merch.html",{'merch':product})
def update_use_page(request):
    if request.user.is_authenticated:
        current_user= User .objects.get(id=request.user.id)
        user_form=updateuser_form(request.POST or None,instance=current_user)
        if user_form .is_valid():
            user_form.save()
            login(request,current_user)
            messages.success(request,'your profile is updated')
            return redirect('pages:home')
        
        context=  {"user_form":user_form} 
        return render(request,'pages/update_user.html',context)
    else:
           messages.success(request,'you shold kbe log in')
           return redirect('pages:home')

def update_pass_page(request):
     return render(request,"pages/update_pass.html")
def ch_pass_page(request):
    if request.user.is_authenticated:
        current_user=request.user
        if request.method=="POST":
            form=updatepasswordform(current_user,request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"password editing")
                login(request,current_user)
                return redirect("pages:update_user")  
            else:
                    messages.success(request,"password inavalabe")
                    return redirect("pages:update_pass")  



        else:
            form=updatepasswordform(current_user)
            context={'form':form}

            return render(request,"pages/ch_pass.html",context) 
    else:
        messages.success(request,"you sould be log in")
        return redirect("pages:login")    
    return render(request,"pages/ch_pass.html",{})