# Generated by Django 3.0.5 on 2021-12-10 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0010_auto_20211210_0225'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='pizza',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='toppings',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
