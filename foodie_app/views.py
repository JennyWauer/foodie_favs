from django.shortcuts import render, redirect

from .models import *

from login.models import User

import json

from django.http import HttpResponse

def home(request):
    if 'userid' in request.session:
        context = {
            "user": User.objects.get(id=request.session['userid'])
        }
        return render(request, 'home.html', context)
    return redirect('/login')

def new_recipe(request):
    if 'userid' in request.session:
        context = {
            "user": User.objects.get(id=request.session['userid'])
        }
        return render(request, 'new_recipe.html', context)
    return redirect('/login')

def user_profile(request, user_id):
    if 'userid' in request.session:
        context = {
            "user": User.objects.get(id=request.session['userid']),
            "recipes": Recipe.objects.all(),
        }
        ingredient_list = Ingredient.objects.all()
        step_list = Step.objects.all()
        print(ingredient_list)
        print(step_list)
        return render(request, 'user_profile.html', context)
    return redirect('/login')

def add_item(request):
    if request.method == 'POST':
        Shopping_List_Item.objects.create(item = request.POST['item'])
        return redirect('/')

def log_off(request):
    request.session.clear()
    return redirect('/')

def add_recipe(request):
    if request.method == "POST":
        Recipe.objects.create(name=request.POST['name'],desc=request.POST['desc'],ingredients=request.POST['ingredients'],steps=request.POST['steps'],user=User.objects.get(id=request.POST['user_id']))
        return redirect('/home')