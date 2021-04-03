from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import *

from login.models import User

from django.contrib import messages

import json

from django.http import HttpResponse, JsonResponse

# GET Requests

def home(request):
    if 'userid' in request.session:
        context = {
            "user": User.objects.get(id=request.session['userid']),
            "recipes": Recipe.objects.all(),
            "users": User.objects.all(),
        }
        return render(request, 'home.html', context)
    return redirect('/login')

def user_profile(request, user_id):
    if 'userid' in request.session:
        menus = Menu.objects.filter(editor=User.objects.get(id=request.session['userid']))
        menu = menus.last()
        context = {
            "user": User.objects.get(id=request.session['userid']),
            "recipes": Recipe.objects.filter(creator=User.objects.get(id=request.session['userid'])),
            "menu": menu,
            "shopping_list": Shopping_List_Item.objects.all(),
            "user_profile": User.objects.get(id=user_id),
        }
        return render(request, 'user_profile.html', context)
    return redirect('/login')

def profile_settings(request, user_id):
    if 'userid' in request.session:
        
        context = {
            "user": User.objects.get(id=request.session['userid']),
        }
        return render(request, 'profile_settings.html', context)
    return redirect('/login')

# RECIPE
def recipe_page(request, recipe_id):
    if 'userid' in request.session:
        context = {
            "user": User.objects.get(id=request.session['userid']),
            "recipe": Recipe.objects.get(id=recipe_id)
        }
        return render(request, 'recipe.html', context)
    return redirect('/')

def new_recipe(request):
    if 'userid' in request.session:
        context = {
            "user": User.objects.get(id=request.session['userid'])
        }
        return render(request, 'new_recipe.html', context)
    return redirect('/login')

def edit_recipe_page(request, recipe_id):
    if 'userid' in request.session:
        context = {
            "user": User.objects.get(id=request.session['userid']),
            "recipe": Recipe.objects.get(id=recipe_id)
        }
        return render(request, 'edit_recipe.html', context)
def delete_recipe(request, recipe_id):
    recipe_to_delete = Recipe.objects.get(id=recipe_id)
    recipe_to_delete.delete()
    return redirect('/home')

# MENU
def menu(request):
    if 'userid' in request.session:
        context = {
            "user": User.objects.get(id=request.session['userid']),
            "recipes": Recipe.objects.all(),
        }
        return render(request, 'menu.html', context)

def previous_menus(request, user_id):
    if 'userid' in request.session:
        context = {
            "user": User.objects.get(id=request.session['userid']),
            "menus": Menu.objects.all(),
            "recipes": Recipe.objects.all(),
        }
        return render(request, 'previous_menus.html', context)

def edit_menu_page(request, menu_id):
    if 'userid' in request.session:
        context = {
            "user": User.objects.get(id=request.session['userid']),
            "menu": Menu.objects.get(id=menu_id),
            "recipes": Recipe.objects.all(),
        }
        return render(request, 'edit_menu.html', context)

# INBOX 
def inbox(request, user_id):
    if 'userid' in request.session:
        context = {
            "user": User.objects.get(id=request.session['userid']),
            "messages": Message.objects.all()
        }
        return render(request, 'inbox.html', context)

def new_message(request, user_id):
    if 'userid' in request.session:
        context = {
            "user": User.objects.get(id=request.session['userid']),
            'all_users': User.objects.all(),

        }
        return render(request, 'new_message.html', context)

def message(request, user_id, message_id):
    if 'userid' in request.session:
        context = {
            "user": User.objects.get(id=request.session['userid']),
            'message': Message.objects.get(id=message_id),
            'all_users': User.objects.all(),
        }
        return render(request, 'message.html', context)  

# ADD AND REMOVE FAVORITES
def add_favorite(request, recipe_id):
    recipe_to_fav = Recipe.objects.get(id=recipe_id)
    user_who_liked = User.objects.get(id=request.session['userid'])
    recipe_to_fav.users_who_favorite.add(user_who_liked)
    recipe_to_fav.save()
    return redirect(f'/home/recipe_{recipe_id}')

def remove_favorite(request, recipe_id):
    recipe_to_remove = Recipe.objects.get(id=recipe_id)
    user_to_remove = User.objects.get(id=request.session['userid'])
    recipe_to_remove.users_who_favorite.remove(user_to_remove)
    recipe_to_remove.save()
    return redirect(f'/home/recipe_{recipe_id}')

def remove_favorite_profile(request, user_id):
    if request.method == "POST":
        recipe_to_remove = Recipe.objects.get(id=request.POST['recipe_id'])
        user_to_remove = User.objects.get(id=request.POST['user_id'])
        recipe_to_remove.users_who_favorite.remove(user_to_remove)
        recipe_to_remove.save()
        return redirect(f'/home/{user_id}')

def add_favorite_home(request, recipe_id):
    recipe_to_fav = Recipe.objects.get(id=recipe_id)
    user_who_liked = User.objects.get(id=request.session['userid'])
    recipe_to_fav.users_who_favorite.add(user_who_liked)
    recipe_to_fav.save()
    return redirect(f'/home/')

def remove_favorite_home(request, recipe_id):
        recipe_to_remove = Recipe.objects.get(id=recipe_id)
        user_to_remove = User.objects.get(id=request.session['userid'])
        recipe_to_remove.users_who_favorite.remove(user_to_remove)
        recipe_to_remove.save()
        return redirect(f'/home')

def log_off(request):
    request.session.clear()
    return redirect('/')

# POST Requests
# RECIPE
def add_recipe(request):
    if request.method == "POST":
        errors = Recipe.objects.recipe_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/home/new_recipe')
        else:
            Recipe.objects.create(
                name=request.POST['name'],
                desc=request.POST['desc'],
                ingredients=request.POST['ingredients'],
                steps=request.POST['steps'],
                creator=User.objects.get(id=request.POST['user_id']),
                source=request.POST['source'])
            return redirect('/home')

def edit_recipe(request, recipe_id):
    if request.method == "POST":
        recipe_to_edit = Recipe.objects.get(id=request.POST['recipe_id'])
        recipe_to_edit.desc = request.POST['desc']
        recipe_to_edit.ingredients = request.POST['ingredients']
        recipe_to_edit.steps = request.POST['steps']
        recipe_to_edit.source = request.POST['source']
        recipe_to_edit.save()
        return redirect(f'/home/recipe_{recipe_id}')

# MENU
def create_menu(request):
    if request.method == "POST":
        Menu.objects.create(
            week_start=request.POST['week_start'],
            sunday=Recipe.objects.get(id=request.POST['sunday']),
            monday=Recipe.objects.get(id=request.POST['monday']),
            tuesday=Recipe.objects.get(id=request.POST['tuesday']),
            wednesday=Recipe.objects.get(id=request.POST['wednesday']),
            thursday=Recipe.objects.get(id=request.POST['thursday']),
            friday=Recipe.objects.get(id=request.POST['friday']),
            saturday=Recipe.objects.get(id=request.POST['saturday']),
            editor=User.objects.get(id=request.POST['user_id'])),
        return redirect('/home')

def edit_menu(request, user_id):
    if request.method == 'POST':
        menu_to_edit = Menu.objects.get(id=request.POST['menu_id'])
        menu_to_edit.sunday = Recipe.objects.get(id=request.POST['sunday'])
        menu_to_edit.monday = Recipe.objects.get(id=request.POST['monday'])
        menu_to_edit.tuesday = Recipe.objects.get(id=request.POST['tuesday'])
        menu_to_edit.wednesday = Recipe.objects.get(id=request.POST['wednesday'])
        menu_to_edit.thursday = Recipe.objects.get(id=request.POST['thursday'])
        menu_to_edit.friday = Recipe.objects.get(id=request.POST['friday'])
        menu_to_edit.saturday = Recipe.objects.get(id=request.POST['saturday'])
        menu_to_edit.week_start = request.POST['week_start']
        menu_to_edit.save()
        return redirect(f'/home/{user_id}')

# SHOPPING LIST
def add_item(request):
    if request.method == 'POST':
        Shopping_List_Item.objects.create(item = request.POST['item'])
        return redirect('/')

@csrf_exempt
def add_item(request):
    if request.method == 'POST':
        user_id = User.objects.get(id=request.session['userid'])
        user_id = user_id.id
        errors = Shopping_List_Item.objects.list_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/home/{user_id}')
        else:
            item = request.POST.get('item')
            user = User.objects.get(id=request.session['userid'])
            shopping_list_item_model, created = Shopping_List_Item.objects.get_or_create(item=item, user=user)
            shopping_list_item_model.save()
            return redirect(f'/home/{user_id}')

def delete_item(request, user_id, item_id):
    item_to_delete = Shopping_List_Item.objects.get(id=item_id)
    item_to_delete.delete()
    return redirect(f'/home/{user_id}')

# PROFILE SETTINGS
def update_profile(request, user_id):
    if request.method == "POST":
        profile_to_edit = User.objects.get(id=user_id)
        profile_to_edit.first_name = request.POST['first_name']
        profile_to_edit.last_name = request.POST['last_name']
        profile_to_edit.email = request.POST['email']
        profile_to_edit.profile_desc = request.POST['profile_desc']
        profile_to_edit.save()
        return redirect(f'/home/{user_id}')

# INBOX
def send_message(request, user_id):
    if request.method == 'POST':
        errors = Message.objects.validate(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/home/{user_id}/inbox')
        else:
            Message.objects.create(
                subject=request.POST['subject'],
                message=request.POST['message'],
                sender=User.objects.get(id=user_id),
                recipient=User.objects.get(id=request.POST['recipient'])
            )
            return redirect(f'/home/{user_id}/inbox')

def delete_message(request, user_id, message_id):
    message_to_delete = Message.objects.get(id=message_id)
    message_to_delete.delete()
    return redirect(f'/home/{user_id}/inbox')

@csrf_exempt
def reply(request, user_id, message_id):
    if request.method == 'POST':
        new_message = Message.objects.create(
            subject=request.POST['subject'],
            message=request.POST['message'],
            sender=User.objects.get(id=user_id),
            recipient=User.objects.get(id=request.POST['recipient_id']),
        )
        original_message = Message.objects.get(id=message_id)
        original_message.replies.add(new_message.id)
        return redirect(f'/home/{user_id}/inbox/{message_id}')