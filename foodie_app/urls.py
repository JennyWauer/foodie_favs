from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('<int:user_id>', views.user_profile),
    path('add_recipe', views.add_recipe),
    path('new_recipe', views.new_recipe),
    path('delete_recipe', views.delete_recipe),
    path('recipe_<int:recipe_id>', views.recipe_page),
    path('edit_<int:recipe_id>', views.edit_recipe),
    path('<int:recipe_id>/edit', views.edit),
    path('<int:recipe_id>/add_favorite', views.add_favorite),
    path('<int:recipe_id>/remove_favorite', views.remove_favorite),
    path('menu', views.menu),
    path('create_menu', views.create_menu),
    path('edit_menu<int:menu_id>', views.edit_menu_page),
    path('<int:user_id>/edit_menu', views.edit_menu),
    path('<int:user_id>/add_item', views.add_item),
    path('<int:user_id>/delete_item', views.delete_item),
    path('<int:user_id>/remove_favorite_profile', views.remove_favorite_profile),
    path('log_off', views.log_off),
    path('<int:user_id>/settings', views.profile_settings),
    path('<int:user_id>/update_profile', views.update_profile),
    # path('add_ingredient', views.add_ingredient),
    # path('add_step', views.add_step),
]