import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django
django.setup()

from pizzas.models import Pizza, Toppings

pizzas_object = Pizza.objects.all()

for pizza in pizzas_object:
    print(pizza.id)
    #don't need pizza.name because we did the __str__ return
    print(pizza)
    print(pizza.date_added)

p = Pizza.objects.get(id=1)
print(p)

toppings = p.toppings_set.all()

for t in toppings:
    print(t)