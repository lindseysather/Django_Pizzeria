#We import the path and include function to include default 
#authenticationnn URLs that Django has defined

from django.urls import path, include

from . import views

app_name = 'users'

urlpatterns = [
    #Include default auth urls
    path('', include('django.contrib.auth.urls')),
    #Registration page
    path('register/',views.register,name='register'),
    ]