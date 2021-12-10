from django.contrib import admin
#from .models import Image

# Register your models here.
from .models import Pizza, Toppings, Image

admin.site.register(Pizza)
admin.site.register(Toppings)
admin.site.register(Image)