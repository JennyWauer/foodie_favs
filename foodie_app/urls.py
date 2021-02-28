from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('new_recipe', views.new_recipe),
    path('<int:user_id>', views.user_profile),
    path('add_item', views.add_item),
    path('add_recipe', views.add_recipe),
    path('log_off', views.log_off),
    path('delete_recipe', views.delete_recipe),
    path('recipe_<int:recipe_id>', views.recipe_page),
    path('add_ingredient', views.add_ingredient),
]