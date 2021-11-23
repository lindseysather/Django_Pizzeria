from django.shortcuts import render

# Create your views here.
def index(request):
#get and pull are the two types of requests
    return render(request, 'pizzas/index.html')