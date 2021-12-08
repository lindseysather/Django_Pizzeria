from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    '''Register a new user.'''
    #if get request, load up blank form 
    if request.method != 'POST':
        form = UserCreationForm()

    #if post request, data user fills out on form is saved to database on form object
    else:
        form = UserCreationForm(data=request.POST)
        #validate
        if form.is_valid():
            new_user = form.save()
            login(request,new_user)
            return redirect('pizzas:index')

    context = {'form':form}
    return render(request,'registration/register.html', context)
