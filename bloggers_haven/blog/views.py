from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def signup(req):
    if req.method == "POST":
        username=req.POST['username']
        password=req.POST['password']
        password2=req.POST['password']

        if password ==password2:
            if User.objects.filter(username=username).exists():
                messages.error(req, "Username already taken")
            else:
                user=User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(req, "Account created successfully")
                return redirect('login')
        else:
            messages.error(req,"Password donot match")

        return render(req, 'blog/signup.html')
    
def login(req):
        if req.method == "POST":
            username=req.POST['username']
            password=req.POST['password']
            user=authenticate(req, username=username, password=password)

            if user is not None:
                login(req,user)
                return redirect('Home')
            else:
                messages.error(req, "Invalid username or password")
        
        return render(req,'blog/login.html')
    
def logout(req):
        logout(req)
        return redirect('home')

@login_required
def home(req):
     return render(req,'blog/home.html')
    
    