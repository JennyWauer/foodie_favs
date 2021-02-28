from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import *

from login.models import User

import json

from django.http import HttpResponse, JsonResponse

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
            "recipes": User.objects.get(id=request.session['userid']).recipes.all(),
        }
        return render(request, 'user_profile.html', context)
    return redirect('/login')

@csrf_exempt
def add_recipe(request):
    if request.method == "POST":
        ingredients = request.POST.get('ingredients')
        ingredients = json.loads(ingredients)
        steps = request.POST.get('steps')
        steps = json.loads(steps)
        name = request.POST.get('name')
        recipe_name = json.loads(name)
        user_for_recipe = request.POST.get('user')

        recipe_model, created = Recipe.objects.get_or_create(name=recipe_name['name'], user=user_for_recipe['user'])

        # for ingredient in ingredients:
        #     ingredient_model, created = Ingredient.objects.get_or_create(ingredient=ingredient['ingredient'], amount=ingredient['amount'])
        #     ingredient_model.save()
        #     # new_recipe.ingredients.add(ingredient_model)
        #     return JsonResponse({'status':200, 'created': created})

        # for step in steps:
        #     step_model, created = Step.objects.get_or_create(step=step['step'])
        #     step_model.save()
        #     # new_recipe.step.add(step_model)
        #     return JsonResponse({'status':200, 'created': created})

def add_item(request):
    if request.method == 'POST':
        Shopping_List_Item.objects.create(item = request.POST['item'])
        return redirect('/')

def log_off(request):
    request.session.clear()
    return redirect('/')

@csrf_exempt
def add_ingredient(request):
    print("successful request")
    if request.method == "POST":
        quantity = request.POST.get('quantity')
        print('Quantity: ' + quantity)
        measurement = request.POST.get('measurement')
        name = request.POST.get('name')
        ingredient_model, created = Ingredient.objects.get_or_create(quantity=quantity, measurement=measurement, name=name)
        ingredient_model.save()
        return HttpResponse("It worked!")

@csrf_exempt
def add_step(request):
    if request.method == "POST":
        step = request.POST.get('step')
        step_number = request.POST.get('step_number')
        print(step_number)
        step_number = int(step_number)
        step_model, created = Step.objects.get_or_create(step=step, step_number=step_number)
        step_model.save()
        return HttpResponse("It worked!")


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