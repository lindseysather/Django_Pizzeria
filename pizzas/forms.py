from django import forms

from .models import Pizza, Toppings, Image

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['name']
        labels = {'name':''}

class ToppingsForm(forms.ModelForm):
    class Meta: 
        model = Toppings
        fields = ['name']
        labels = {'name':''}

class ImageForm(forms.ModelForm):
    '''Form for the image model'''
    class Meta:
        model = Image
        fields = ('title', 'image')

