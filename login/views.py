from django.shortcuts import render, redirect

from .models import *

from django.contrib import messages

import bcrypt

def foodie_favs(request):
    return render(request, 'foodie_favs.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def new_user(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if User.objects.filter(email=request.POST['email']):
            messages.error(request, 'Email is already registered. Please login!')
            return redirect('/login')
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/login')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()    
            new_user = User.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                password=pw_hash
            )
            request.session['userid'] = new_user.id
            return redirect('/home')
    return redirect('/login')

def user_login(request):
    if request.method == 'GET':
        return redirect('/')
    if request.method == 'POST':
        user = User.objects.filter(email=request.POST['login_email'])
        if user:
            logged_user = user[0] 
            if bcrypt.checkpw(request.POST['login_pass'].encode(), logged_user.password.encode()):
                request.session['userid'] = logged_user.id
                return redirect('/register')
        else:
            messages.error(request, 'Email/password combination not recognized. Please try again!')
        return redirect("/login")

def home(request):
    return redirect('/login')