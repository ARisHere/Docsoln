from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    
    path("", views.index, name='home'),
    path("home", views.index, name='home'),
    path("appointment", views.appointment, name='appointment'),
    path("ambulance", views.ambulance, name='ambulance'),
    path("login", views.login, name='login'),
    path("medicine", views.medicine, name='medicine'),
    path("blooddonnor", views.blooddonnor, name='blooddonnor'),
    path("donnerinfo", views.donnerinfo, name='donnerinfo'),
    path("docprofile", views.docprofile, name='docprofile'),
    path("bookinfo", views.bookinfo, name='bookinfo'),
]
