from django.urls import path

from . import views

app_name = 'pizzas'

urlpatterns = [
    path('', views.index, name='index'),
    path('pizzas_object', views.pizzas_object, name='pizzas_object'),
]