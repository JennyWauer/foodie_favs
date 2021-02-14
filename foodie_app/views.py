from django.shortcuts import render, redirect

from .models import *

from login.models import User

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
            "user": User.objects.get(id=request.session['userid'])
        }
        return render(request, 'user_profile.html', context)
    return redirect('/login')

def add_recipe(request):
    if request.method == "POST":
        new_recipe = Recipe.objects.create(name=request.POST['name'])
        for instance in request.POST['ingredient'].all():
            new_ingredient = Ingredient.objects.create(amount=request.POST['amount'], name=request.POST['ingredient'])