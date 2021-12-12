from django.shortcuts import render, redirect

'''from class'''
from pizzas.forms import ImageForm, CommentForm
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
    comments = pizza.comment_set.all()
    images = pizza.image_set.all()

    #key represents variable name in template
    #value represents variable name view 
    context = {'pizza':pizza, 'toppings':toppings, 'comments':comments, 'images':images}

    return render(request, 'pizzas/pizza.html', context)


def image_upload_view(request):
    """Process images uploaded"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            context = {'form':form, 'pizza':pizza}
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj}, context)
    else:
        form = ImageForm()
    context = {'form':form, 'pizza':pizza}
    return render(request, 'index.html', {'form': form}, context)

 

def new_comment(request, pizza_id, user_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)

        if form.is_valid():
            #False will make it not write to the database yet
            new_comment = form.save(commit=False)
            new_comment.pizza = pizza
            new_comment.save()

            return redirect('pizzas:pizza', pizza_id=pizza_id, user_id=user_id)

    context = {'form':form, 'pizza':pizza}
    return render(request, 'pizzas/new_comment.html', context)
