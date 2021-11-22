from django.db import models

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    #shows text of name object:
    def __str__(self):
        return self.name

class Toppings(models.Model):
    #pizza is a foreign key to Pizza
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    #name can hold values (pineapple, sausage, etc.)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)