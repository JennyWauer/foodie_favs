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

def add_recipe(request):
    if request.method == "POST":
        ingredients = request.POST.get('ingredients')
        ingredients = json.loads(ingredients)
        steps = request.POST.get('steps')
        steps = json.loads(steps)
        recipe_name = request.POST.get('name')
        recipe_name = json.loads(name)
        user_for_recipe = request.POST.get('user')

        recipe_model, Recipe.objects.get_or_create(name=recipe_name['name'], user=user_for_recipe[user])

        for ingredient in ingredients:
            ingredient_model, created = Ingredient.objects.get_or_create(ingredient=ingredient['ingredient'], amount=ingredient['amount'])
            # new_recipe.ingredients.add(ingredient_model)
            return JsonResponse({'status':200, 'created': created})

        for step in steps:
            step_model, created = Step.objects.get_or_create(step=step['step'])
            # new_recipe.step.add(step_model)
            return JsonResponse({'status':200, 'created': created})

def add_item(request):
    if request.method == 'POST':
        Shopping_List_Item.objects.create(item = request.POST['item'])
        return redirect('/')

def log_off(request):
    request.session.clear()
    return redirect('/')

def add_ingredient(request):
    print("successful request")
    if request.method == "POST":
        quantity = request.POST.get('quantity')
        print(quantity)
        quantity = json.loads(quantity)
        measurement = request.POST.get('measurement')
        measurement = json.loads(measurement)
        name = request.POST.get('name')
        name = json.loads(ingredients)
        ingredient_model, created = Ingredient.objects.get_or_create(quantity=quantity['quantity'], measurement=measurement['measurement'], name=name['name'])
        ingredient_model.save()
        return HttpResponse("It worked!")

def add_step(request):
    if request.method == "POST":
        Step.objects.create(step=request.POST['step'])