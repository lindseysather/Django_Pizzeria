from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    #shows text of name object:
    def __str__(self):
        return self.name

class Toppings(models.Model):
    #pizza is a foreign key to Pizza
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    #name can hold values (pineapple, sausage, etc.)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    #returns toppings (pineapple, ham) as text (instead of Topping Object (1))
    #string method
    def __str__(self):
        return self.name
        #after we wrote this, we makemigrations and migrate because we change something 


class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        #returns first 50 characters of text
        return self.name
     

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

