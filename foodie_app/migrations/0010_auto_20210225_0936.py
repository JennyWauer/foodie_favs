# Generated by Django 2.2 on 2021-02-25 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodie_app', '0009_step_step_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='quantity',
            field=models.CharField(max_length=255),
        ),
    ]
