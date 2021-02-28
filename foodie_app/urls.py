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
    path('edit_<int:recipe_id>', views.edit_recipe),
    path('edit', views.edit),
    path('add_favorite', views.add_favorite),
    path('remove_favorite', views.remove_favorite),
    path('menu', views.menu),
    path('create_menu', views.create_menu),
    path('edit_menu<int:menu_id>', views.edit_menu_page),
    # path('add_ingredient', views.add_ingredient),
    # path('add_step', views.add_step),
]