from django.shortcuts import render, redirect
# from django.views.decorators.csrf import csrf_exempt

from .models import *

from login.models import User

# import json

# from django.http import HttpResponse, JsonResponse

def home(request):
    if 'userid' in request.session:
        context = {
            "user": User.objects.get(id=request.session['userid']),
            "recipes": Recipe.objects.all(),
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
            "recipes": Recipe.objects.filter(creator=User.objects.get(id=request.session['userid'])),
            "menu": Menu.objects.get(id=1)
        }
        return render(request, 'user_profile.html', context)
    return redirect('/login')

def add_item(request):
    if request.method == 'POST':
        Shopping_List_Item.objects.create(item = request.POST['item'])
        return redirect('/')

def log_off(request):
    request.session.clear()
    return redirect('/')

def delete_recipe(request):
    if request.method == "POST":
        recipe_to_delete = Recipe.objects.get(id=request.POST['recipe_id'])
        recipe_to_delete.delete()
        return redirect('/home')

def recipe_page(request, recipe_id):
    if 'userid' in request.session:
        context = {
            "user": User.objects.get(id=request.session['userid']),
            "recipe": Recipe.objects.get(id=recipe_id)
        }
        return render(request, 'recipe.html', context)
    return redirect('/')

def add_recipe(request):
    if request.method == "POST":
        Recipe.objects.create(name=request.POST['name'],desc=request.POST['desc'],ingredients=request.POST['ingredients'],steps=request.POST['steps'],creator=User.objects.get(id=request.POST['user_id']),source=request.POST['source'])
        return redirect('/home')

def edit_recipe(request, recipe_id):
    if 'userid' in request.session:
        context = {
            "user": User.objects.get(id=request.session['userid']),
            "recipe": Recipe.objects.get(id=recipe_id)
        }
        return render(request, 'edit_recipe.html', context)

def edit(request):
    if request.method == "POST":
        recipe_to_edit = Recipe.objects.get(id=request.POST['recipe_id'])
        recipe_to_edit.desc = request.POST['desc']
        recipe_to_edit.ingredients = request.POST['ingredients']
        recipe_to_edit.steps = request.POST['steps']
        recipe_to_edit.source = request.POST['source']
        recipe_to_edit.save()
        return redirect("/home") #try to redirect back to recipe...

def add_favorite(request):
    if request.method == "POST":
        recipe_to_fav = Recipe.objects.get(id=request.POST['recipe_id'])
        user_who_liked = User.objects.get(id=request.POST['user_id'])
        recipe_to_fav.users_who_favorite.add(user_who_liked)
        recipe_to_fav.save()
        return redirect('/home')

def remove_favorite(request):
    if request.method == "POST":
        recipe_to_remove = Recipe.objects.get(id=request.POST['recipe_id'])
        user_to_remove = User.objects.get(id=request.POST['user_id'])
        recipe_to_remove.users_who_favorite.remove(user_to_remove)
        recipe_to_remove.save()
        return redirect('/home')

def menu(request):
    if 'userid' in request.session:
        context = {
            "user": User.objects.get(id=request.session['userid']),
            "recipes": Recipe.objects.all(),
        }
        return render(request, 'menu.html', context)

def create_menu(request):
    if request.method == "POST":
        Menu.objects.create(sunday=Recipe.objects.get(id=request.POST['sunday']),monday=Recipe.objects.get(id=request.POST['monday']),tuesday=Recipe.objects.get(id=request.POST['tuesday']),wednesday=Recipe.objects.get(id=request.POST['wednesday']),thursday=Recipe.objects.get(id=request.POST['thursday']),friday=Recipe.objects.get(id=request.POST['friday']), saturday=Recipe.objects.get(id=request.POST['saturday']))
        return redirect('/home')