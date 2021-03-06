from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('<int:user_id>', views.user_profile),
    # RECIPE
    path('recipe_<int:recipe_id>', views.recipe_page),
    path('new_recipe', views.new_recipe),
    path('<int:recipe_id>/edit_recipe_page', views.edit_recipe_page),
    path('<int:recipe_id>/delete_recipe', views.delete_recipe),
    path('add_recipe', views.add_recipe),
    path('<int:recipe_id>/edit_recipe', views.edit_recipe),
    # MENU
    path('menu', views.menu),
    path('<int:user_id>/previous_menus', views.previous_menus),
    path('edit_menu<int:menu_id>', views.edit_menu_page),
    path('create_menu', views.create_menu),
    path('<int:user_id>/edit_menu', views.edit_menu),
    # SHOPPING LIST
    path('add_item', views.add_item),
    path('<int:user_id>/delete_item/<int:item_id>', views.delete_item),
    # USER PROFILE
    path('<int:user_id>/settings', views.profile_settings),
    path('<int:user_id>/update_profile', views.update_profile),
    # INBOX
    path('<int:user_id>/inbox', views.inbox),
    path('<int:user_id>/new_message', views.new_message),
    path('<int:user_id>/inbox/<int:message_id>', views.message),
    path('<int:user_id>/send_message', views.send_message),
    path('<int:user_id>/<int:message_id>/delete_message', views.delete_message),
    path('<int:user_id>/inbox/<int:message_id>/reply', views.reply),
    # ADD AND REMOVE FAVORITES
    path('<int:recipe_id>/add_favorite', views.add_favorite),
    path('<int:recipe_id>/remove_favorite', views.remove_favorite),
    path('<int:user_id>/remove_favorite_profile', views.remove_favorite_profile),
    path('<int:recipe_id>/remove_favorite_home', views.remove_favorite_home),
    path('<int:recipe_id>/add_favorite_home', views.add_favorite_home),
    # LOG OFF
    path('log_off', views.log_off),
    # path('add_ingredient', views.add_ingredient),
    # path('add_step', views.add_step),
]