from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from pastelitos.views import *
from .views import *
from . import views

urlpatterns = [
    path('', views.hola, name="hola"),

]