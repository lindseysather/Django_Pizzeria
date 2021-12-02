from django.urls import path

from . import views

app_name = 'pizzas'

urlpatterns = [
    path('', views.index, name='index'),

    #makes url 127.0.0.1:8000/pizzas_object
    path('pizzas_object', views.pizzas_object, name='pizzas_object'),
    path('pizzas_object/<int:pizza_id>/', views.pizza, name='pizza'),
    path('new_pizza/',views.new_pizza, name='new_pizza'),
    path('new_topping/<int:pizza_id>/', views.new_topping, name='new_topping'),
]