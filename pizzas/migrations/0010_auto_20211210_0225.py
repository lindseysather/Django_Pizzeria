# Generated by Django 3.0.5 on 2021-12-10 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0009_auto_20211210_0224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='toppings',
            name='date_added',
        ),
    ]
