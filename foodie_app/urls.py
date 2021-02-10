from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('new_recipe', views.new_recipe),
    path('<int:user_id>', views.user_profile),
]