# Generated by Django 2.2 on 2021-02-12 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodie_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='amount',
            field=models.CharField(default='', max_length=10),
        ),
    ]
