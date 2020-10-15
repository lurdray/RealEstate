from django.urls import path, include
from . import views

#app_name = 'nigtech'

urlpatterns = [

    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('properties/', views.properties, name='properties'),
    path('contact/', views.contact, name='contact'),

    ]