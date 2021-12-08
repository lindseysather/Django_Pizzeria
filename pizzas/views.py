from django.shortcuts import render, redirect

'''from class'''
from pizzas.forms import ToppingsForm, PizzaForm 

from .models import Pizza

# Create your views here.
def index(request):
#get and pull are the two types of requests
    return render(request, 'pizzas/index.html')

def pizzas_object(request):
    pizzas_object = Pizza.objects.order_by('date_added')
    
    #key is the variable used in the template/html file
    #value is the variable used in the view function
    context = {'pizzas_object':pizzas_object}

    return render(request, 'pizzas/pizzas_object.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    
    toppings = pizza.toppings_set.all()

    #key represents variable name in template
    #value represents variable name view
    context = {'pizza':pizza, 'toppings':toppings}

    return render(request, 'pizzas/pizza.html', context)

'''
def new_pizza(request):
    #if request is a get method
    if request.method != 'POST':
        form = PizzaForm()
    else:
        form = PizzaForm(data=request.POST)

        if form.is_valid():
            form.save()

            return redirect('pizzas:pizzas_object')

    #know what context is for final
    context = {'form':form}
    return render(request, 'pizzas/new_pizza.html', context)


def new_topping(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = ToppingsForm()
    else:
        form = ToppingsForm(data=request.POST)

        if form.is_valid():
            #False will make it not write to the database yet
            new_topping = form.save(commit=False)
            new_topping.pizza = pizza
            
            new_topping.save()

            return redirect('pizzas:pizza', pizza_id=pizza_id)

    context = {'form':form, 'pizza':pizza}
    return render(request, 'pizzas/new_topping.html', context)
'''