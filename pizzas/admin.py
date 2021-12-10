from django.contrib import admin
#from .models import Image

# Register your models here.
from .models import Pizza, Toppings, Image, Comment

admin.site.register(Pizza)
admin.site.register(Toppings)
admin.site.register(Image)
admin.site.register(Comment)