from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('calc/',views.calculator,name='calc'),
    
       
]
