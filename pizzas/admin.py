from django.contrib import admin

# Register your models here.
from .models import Pizza, Toppings, Image, Comment

admin.site.register(Pizza)
admin.site.register(Toppings)
admin.site.register(Image)
admin.site.register(Comment)