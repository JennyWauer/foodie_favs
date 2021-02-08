from django.db import models
import re

# Create your models here.


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        email_check = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        password = postData['password']
        conf_password = postData['conf_password']
        if len(postData['first_name']) < 2:
            errors["first_name"] = "Your first name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "You last name should be at least 3 characters"
        if not email_check.match(postData['email']):
            errors["email"] = "Your email should be a valid email"
        email_exist = self.filter(email=postData['email'])
        if email_exist:
            errors['email'] = "Email already in use"
        if len(postData['password']) < 8:
            errors["password_len"] = "Your password should be at least 8 characters"
        if not password == conf_password:
            errors["password"] = "Your passwords do not match"
        return errors

    def login_validator(self, postData):
        login_errors = {}
        login_pass = postData['login_pass']
        login_email = postData['login_email']
        if len(User.objects.filter(email=login_email)) < 0:
            errors["login_email"] = "User email not found"
        if len(User.objects.filter(email=login_email)) > 0:
            user = User.objects.get(email=login_email)
            if not user.password == login_pass:
                errors["login_password"] = "Password does not match user email"
        return login_errors
