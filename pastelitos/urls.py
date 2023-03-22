from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from pastelitos.views import *
from .views import *
from . import views

urlpatterns = [
    url(r'^$',landing, name="landing"),
    path('post_pastel/', post_pastel, name="post_pastel"),
    path('detalle_pastel/<int:id>', updatepastel, name="updatepastel"),
    path('postm_pastel/<int:id>', updatepastel, name="postm_pastel"),
    path('sacar_datos/<int:id>', updatepastel,name="postm_pastel"),
    path('removerpastel', removerpastel, name='removerpastel'),

    url('landingcliente/',landingcliente, name="landingcliente"),
    path('post_cliente/', post_cliente, name="post_cliente"),
    path('detalle_cliente/<int:id>', updatecliente, name="updatecliente"),
    path('postm_cliente/<int:id>', updatecliente, name="postm_cliente"),
    path('sacar_datos_cliente/<int:id>', updatecliente,name="postm_cliente"),
    path('removercliente', removercliente, name='removercliente'),


    url('landingproveedor/',landingproveedor, name="landingproveedor"),
    path('post_proveedor/', post_proveedor, name="post_proveedor"),
    path('detalle_proveedor/<int:id>', updateproveedor, name="updateproveedor"),
    path('postm_proveedor/<int:id>', updateproveedor, name="postm_proveedor"),
    path('sacar_datos_proveedor/<int:id>', updateproveedor,name="postm_proveedor"),
    path('removerproveedor',removerproveedor, name='removerproveedor'),
    
    url('landingsucursal/',landingsucursal, name="landingsucursal"),
    path('post_sucursal/', post_sucursal, name="post_sucursal"),
    path('detalle_sucursal/<int:id>', updatesucursal, name="updatesucursal"),
    path('postm_sucursal/<int:id>', updatesucursal, name="postm_sucursal"),
    path('sacar_datos_sucursal/<int:id>', updatesucursal,name="postm_sucursal"),
    path('removersucursal',removersucursal, name='removersucursal'),

    path('practica/',practica, name='practica'), 

]