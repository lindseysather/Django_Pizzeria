# Generated by Django 3.0.5 on 2021-12-11 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0011_auto_20211210_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='pizza',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pizzas.Pizza'),
            preserve_default=False,
        ),
    ]
