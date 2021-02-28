from django.db import models

from login.models import User

# class Ingredient(models.Model):
#     quantity = models.CharField(max_length=255, default="")
#     measurement = models.CharField(max_length=10, default="")
#     name = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

class Menu(models.Model):
    week_start = models.DateField()
    week_end = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255, default="")
    ingredients = models.TextField()
    steps = models.TextField()
    # ingredient = models.ForeignKey(Ingredient, related_name="ingredient_recipes", on_delete = models.CASCADE, default="1")
    menus = models.ManyToManyField(Menu, related_name="menu_recipes", default="1")
    creator = models.ForeignKey(User, related_name="users", on_delete=models.CASCADE, default="1")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Shopping_List_Item(models.Model):
    item = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# class Step(models.Model):
#     step = models.CharField(max_length=255)
#     step_number = models.IntegerField(default=1)
#     recipe = models.ForeignKey(Recipe, related_name="steps", on_delete=models.CASCADE, default=1)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)