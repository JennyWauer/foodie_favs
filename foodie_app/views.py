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