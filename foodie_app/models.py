from django.db import models

from login.models import User

class Ingredient(models.Model):
    amount = models.CharField(max_length=10,default="")
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Step(models.Model):
    step = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Menu(models.Model):
    week_start = models.DateField()
    week_end = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Following(models.Model):
    target = models.ForeignKey(User, related_name="followers", on_delete = models.CASCADE)
    follower = models.ForeignKey(User, related_name="targets", on_delete = models.CASCADE)

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    incredients = models.ForeignKey(Ingredient, related_name="ingredients", on_delete = models.CASCADE)
    steps = models.ForeignKey(Step, related_name="steps", on_delete = models.CASCADE)
    menus = models.ManyToManyField(Menu, related_name="menus")
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE, default="1")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Shopping_List_Item(models.Model):
    item = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)