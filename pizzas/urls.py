from django.urls import path

from . import views

app_name = 'pizzas'

urlpatterns = [
    path('', views.index, name='index'),

    #makes url 127.0.0.1:8000/pizzas_object
    path('pizzas_object', views.pizzas_object, name='pizzas_object'),
    path('pizzas_object/<int:pizza_id>/', views.pizza, name='pizza'),

]