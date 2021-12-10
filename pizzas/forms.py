from django import forms

from .models import Pizza, Toppings

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

