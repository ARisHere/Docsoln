from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    
    path("home", views.index, name='home'),
    path("appointment", views.appointment, name='appointment'),
    path("ambulance", views.ambulance, name='ambulance'),
    path("login", views.login, name='login'),
    

    
]
