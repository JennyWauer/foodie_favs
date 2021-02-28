# Generated by Django 2.2 on 2021-02-28 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodie_app', '0002_auto_20210228_0857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='step',
            name='recipe',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='ingredient',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='recipe',
            name='steps',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='login.User'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='menus',
            field=models.ManyToManyField(default=1, related_name='menu_recipes', to='foodie_app.Menu'),
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
        migrations.DeleteModel(
            name='Step',
        ),
    ]
