from django.shortcuts import render, redirect

def home(request):
    if 'userid' in request.session:
        context = {
            "user": User.objects.get(id=request.session['userid'])
        }
        return render(request, 'home.html', context)
    return redirect('/login')

def new_recipe(request):
    return render(request, 'new_recipe.html')

def user_profile(request, user_id):
    if 'userid' in request.session:
        context = {
            "user": User.objects.get(id=request.session['userid'])
        }
        return render(request, 'user_profile.html', context)
    return redirect('/login')