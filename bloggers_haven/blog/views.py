from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Blog




# Create your views here.

def signup_view(req):
    if req.method == "POST":
        username=req.POST['username']
        email=req.POST['email']
        password=req.POST['password']
        confirm_password=req.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(req, "Username already taken")
            elif User.objects.filter(email=email). exists():
                 messages.error(req, "Email already registered!")
            else:
                user=User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(req, "Account created successfully! Please login.")
                return redirect('login')
        else:
            messages.error(req,"Password do not match")

        return render(req, 'blog/signup.html')
    
def login_view(req):
        if req.method == "POST":
            username=req.POST['username']
            password=req.POST['password']
            user=authenticate(req, username=username, password=password)

            if user is not None:
                login(req,user)
                return redirect('home')
            else:
                messages.error(req, "Invalid username or password")
        
        return render(req,'blog/login.html')
    
def logout_view(req):
        logout(req)
        messages.success(req, "You have logged out successfully! ")
        return redirect('home')

@login_required
def home(req):
     return render(req,'blog/home.html')

def create_post(req):
     if req.method == "POST":
          title=req.POST['title']
          content=req.POST['content']
          Blog.objects.create(title=title, content=content)
          return redirect(req, 'post_list')
     return render(req, 'blog/create_post.html')

def post_list(req):
     posts=Blog.objects.all()
     return render(req,'blog/post_list.html', {'list':list})

def update_post(req, post_id):
     post=get_object_or_404(Blog, id=post_id)
     if req.method =="POST":
          post.title=req.POST.get('title')
          post.content=req.POST.get('content')
          post.save()
          return redirect('post_list')
     return render(req,'blog/update_post.thml')

def delete_post(req, post_id):
     post=get_object_or_404(Blog, id=post_id)
     post.delete()
     return redirect('post_list')
    
    