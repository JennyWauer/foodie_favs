from django.db import models

from login.models import User

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    incredients = models.ManyToManyField(Ingredient, related_name="recipies")
    steps = models.ManyToManyField(Step, related_name="recipies")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)