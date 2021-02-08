from django.shortcuts import render

def foodie_favs(request):
    return render(request, 'foodie_favs.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')