from django.shortcuts import render

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