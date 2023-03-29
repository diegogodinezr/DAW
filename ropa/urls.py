from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from ropa.views import *
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    url(r'^$',landingr, name="landingr"),

    url('landingproductor/',landingproductor, name="landingproductor"),
    path('post_productor/', post_productor, name="post_productor"),
    path('detalle_productor/<int:id>', updateproductor, name="updateproductor"),
    path('postm_productor/<int:id>', updateproductor, name="postm_productor"),
    path('sacar_datos_productor/<int:id>', updateproductor,name="postm_productor"),
    path('removerproductor', removerproductor, name='removerproductor'),

    url('landingclienter/',landingclienter, name="landingclienter"),
    path('post_clienter/', post_clienter, name="post_clienter"),
    path('detalle_clienter/<int:id>', updateclienter, name="updateclienter"),
    path('postm_clienter/<int:id>', updateclienter, name="postm_clienter"),
    path('sacar_datos_clienter/<int:id>', updateclienter,name="postm_clienter"),
    path('removerclienter', removerclienter, name='removerclienter'),

    url('landingproveedorr/',landingproveedorr, name="landingproveedorr"),
    path('post_proveedorr/', post_proveedorr, name="post_proveedorr"),
    path('detalle_proveedorr/<int:id>', updateproveedorr, name="updateproveedorr"),
    path('postm_proveedorr/<int:id>', updateproveedorr, name="postm_proveedorr"),
    path('sacar_datos_proveedorr/<int:id>', updateproveedorr,name="postm_proveedorr"),
    path('removerproveedorr', removerproveedorr, name='removerproveedorr'),
    
    url('landingsucursalr/',landingsucursalr, name="landingsucursalr"),
    path('post_sucursalr/', post_sucursalr, name="post_sucursalr"),
    path('detalle_sucursalr/<int:id>', updatesucursalr, name="updatesucursalr"),
    path('postm_sucursalr/<int:id>', updatesucursalr, name="postm_sucursalr"),
    path('sacar_datos_sucursalr/<int:id>', updatesucursalr,name="postm_sucursalr"),
    path('removersucursalr', removersucursalr, name='removersucursalr'),

    url('landingempleador/',landingempleador, name="landingempleador"),
    path('post_empleador/', post_empleador, name="post_empleador"),
    path('detalle_empleador/<int:id>', updateempleador, name="updateempleador"),
    path('postm_empleador/<int:id>', updateempleador, name="postm_empleador"),
    path('sacar_datos_empleador/<int:id>', updateempleador,name="postm_empleador"),
    path('removerempleador', removerempleador, name='removerempleador'),

    url('landingcategoriar/',landingcategoriar, name="landingcategoriar"),
    path('post_categoriar/', post_categoriar, name="post_categoriar"),
    path('detalle_categoriar/<int:id>', updatecategoriar, name="updatecategoriar"),
    path('postm_categoriar/<int:id>', updatecategoriar, name="postm_categoriar"),
    path('sacar_datos_categoriar/<int:id>', updatecategoriar,name="postm_categoriar"),
    path('removercategoriar', removercategoriar, name='removercategoriar'),

    path('logout/',LogoutView.as_view(next_page='/'), name='logout'),
]