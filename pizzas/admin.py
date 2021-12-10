from django.contrib import admin
from .models import images

# Register your models here.
from .models import Pizza, Toppings

admin.site.register(Pizza)
admin.site.register(Toppings)


'''TRYING TO UPLOAD IMAGES'''
class AdminImages(admin.ModelAdmin):
    list_display = ['id_no','name','loc','image','profile']

admin.site.register(images,AdminImages)