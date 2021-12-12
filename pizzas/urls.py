from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
#from uploadimg import views


'''TRYING TO UPLOAD PHOTOS'''
from django.conf import settings
from django.conf.urls.static import static
'''END'''

app_name = 'pizzas'

urlpatterns = [
    path('', views.index, name='index'),

    #makes url 127.0.0.1:8000/pizzas_object
    path('pizzas_object', views.pizzas_object, name='pizzas_object'),
    path('pizzas_object/<int:pizza_id>/', views.pizza, name='pizza'),
    path('upload/', views.image_upload_view),

    #comments
    path('new_comment/<int:pizza_id>/', views.new_comment, name='new_comment'),
]

urlpatterns += staticfiles_urlpatterns()


'''TRYING TO UPLOAD PHOTOS'''
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)