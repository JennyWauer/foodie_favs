# Generated by Django 2.2 on 2021-02-14 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodie_app', '0004_shopping_list'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Shopping_List',
            new_name='Shopping_List_Item',
        ),
    ]
