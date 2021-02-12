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
    incredients = models.ManyToManyField(Ingredient, related_name="recipies")
    steps = models.ManyToManyField(Step, related_name="recipies")
    menus = models.ManyToManyField(Menu, related_name="menus")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)