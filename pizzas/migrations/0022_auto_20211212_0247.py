# Generated by Django 3.0.5 on 2021-12-12 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0021_auto_20211212_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='media/pizzas'),
        ),
    ]
