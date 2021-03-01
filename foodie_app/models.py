from django.db import models

from login.models import User

# class Ingredient(models.Model):
#     quantity = models.CharField(max_length=255, default="")
#     measurement = models.CharField(max_length=10, default="")
#     name = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255, default="")
    ingredients = models.TextField(default="")
    steps = models.TextField(default="")
    # ingredient = models.ForeignKey(Ingredient, related_name="ingredient_recipes", on_delete = models.CASCADE, default="1")
    # menus = models.ManyToManyField(Menu, related_name="menu_recipes", default=1)
    creator = models.ForeignKey(User, related_name="users", on_delete=models.CASCADE, default=1)
    source = models.CharField(max_length=255, default="")
    users_who_favorite = models.ManyToManyField(User, related_name="favorite_recipes", default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Shopping_List_Item(models.Model):
    item = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="list_user", on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Menu(models.Model):
    # week_start = models.DateField()
    # week_end = models.DateField()
    sunday = models.ForeignKey(Recipe, related_name="sunday_recipes", on_delete=models.CASCADE)
    monday = models.ForeignKey(Recipe, related_name="monday_recipes", on_delete=models.CASCADE)
    tuesday = models.ForeignKey(Recipe, related_name="tuesday_recipes", on_delete=models.CASCADE)
    wednesday = models.ForeignKey(Recipe, related_name="wednesday_recipes", on_delete=models.CASCADE)
    thursday = models.ForeignKey(Recipe, related_name="thursday_recipes", on_delete=models.CASCADE)
    friday = models.ForeignKey(Recipe, related_name="friday_recipes", on_delete=models.CASCADE)
    saturday = models.ForeignKey(Recipe, related_name="saturday_recipes", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# class Step(models.Model):
#     step = models.CharField(max_length=255)
#     step_number = models.IntegerField(default=1)
#     recipe = models.ForeignKey(Recipe, related_name="steps", on_delete=models.CASCADE, default=1)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)