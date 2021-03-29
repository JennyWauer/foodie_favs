from django.db import models

from login.models import User

# class Ingredient(models.Model):
#     quantity = models.CharField(max_length=255, default="")
#     measurement = models.CharField(max_length=10, default="")
#     name = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

class RecipeManager(models.Manager):
    def recipe_validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors["name"] = "Recipe name should be at least 2 characters"
        if len(postData['desc']) < 3:
            errors["desc"] = "Recipe description should be at least 3 characters"
        if len(postData['ingredients']) < 3:
            errors["ingredients"] = "Recipe ingredients should be at least 3 characters"
        if len(postData['steps']) < 3:
            errors["steps"] = "Recipe steps should be at least 3 characters"
        return errors

class ListManager(models.Manager):
    def list_validator(self, postData):
        errors = {}
        if len(postData['item']) < 2:
            errors["item"] = "Shopping list item should be at least 2 characters"
        return errors

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
    objects = RecipeManager()

class Shopping_List_Item(models.Model):
    item = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="list_user", on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ListManager()

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
    editor = models.ForeignKey(User, related_name="menus", on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# class Step(models.Model):
#     step = models.CharField(max_length=255)
#     step_number = models.IntegerField(default=1)
#     recipe = models.ForeignKey(Recipe, related_name="steps", on_delete=models.CASCADE, default=1)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

class MessageManager(models.Manager):
    def validate(self, form):
        errors = {}
        if len(form['subject']) < 2:
            errors['subject'] = "Subject field cannon be empty"
        if len(form['message']) < 2:
            errors['description'] = "Message field cannot be empty"
        return errors

class Message(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sender = models.ForeignKey(User, related_name="sent_messages",on_delete = models.CASCADE)
    recipient = models.ForeignKey(User, related_name="received_messages",on_delete = models.CASCADE)
    replies = models.ManyToManyField("self", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()