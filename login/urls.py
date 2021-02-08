from django.urls import path

from . import views

urlpatterns = [
    path('', views.foodie_favs),
    path('register', views.register),
    path('login', views.login),
]