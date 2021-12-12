# Generated by Django 3.0.5 on 2021-12-12 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0013_auto_20211211_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza_Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='photos/')),
            ],
        ),
        migrations.AlterModelTable(
            name='image',
            table='myapp_image',
        ),
    ]