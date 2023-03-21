from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from abarrotes.views import *
from .views import *

urlpatterns = [
    url(r'^$',landinga, name="landinga"),

    url('landingproductoa/',landingproductoa, name="landingproductoa"),
    path('post_productoa/', post_productoa, name="post_productoa"),
    path('detalle_productoa/<int:id>', updateproductoa, name="updateproductoa"),
    path('postm_productoa/<int:id>', updateproductoa, name="postm_productoa"),
    path('sacar_datos_productoa/<int:id>', updateproductoa,name="postm_productoa"),
    path('removerproductoa', removerproductoa, name='removerproductoa'),

    url('landingclientea/',landingclientea, name="landingclientea"),
    path('post_clientea/', post_clientea, name="post_clientea"),
    path('detalle_clientea/<int:id>', updateclientea, name="updateclientea"),
    path('postm_clientea/<int:id>', updateclientea, name="postm_clientea"),
    path('sacar_datos_clientea/<int:id>', updateclientea,name="postm_clientea"),
    path('removerclientea', removerclientea, name='removerclientea'),

    url('landingproveedora/',landingproveedora, name="landingproveedora"),
    path('post_proveedora/', post_proveedora, name="post_proveedora"),
    path('detalle_proveedora/<int:id>', updateproveedora, name="updateproveedora"),
    path('postm_proveedora/<int:id>', updateproveedora, name="postm_proveedora"),
    path('sacar_datos_proveedora/<int:id>', updateproveedora,name="postm_proveedora"),
    path('removerproveedora', removerproveedora, name='removerproveedora'),
    
    url('landingsucursala/',landingsucursala, name="landingsucursala"),
    path('post_sucursala/', post_sucursala, name="post_sucursala"),
    path('detalle_sucursala/<int:id>', updatesucursala, name="updatesucursala"),
    path('postm_sucursala/<int:id>', updatesucursala, name="postm_sucursala"),
    path('sacar_datos_sucursala/<int:id>', updatesucursala,name="postm_sucursala"),
    path('removersucursala', removersucursala, name='removersucursala'),

    url('landingempleadoa/',landingempleadoa, name="landingempleadoa"),
    path('post_empleadoa/', post_empleadoa, name="post_empleadoa"),
    path('detalle_empleadoa/<int:id>', updateempleadoa, name="updateempleadoa"),
    path('postm_empleadoa/<int:id>', updateempleadoa, name="postm_empleadoa"),
    path('sacar_datos_empleadoa/<int:id>', updateempleadoa,name="postm_empleadoa"),
    path('removerempleadoa', removerempleadoa, name='removerempleadoa'),

    url('landingcategoriaa/',landingcategoriaa, name="landingcategoriaa"),
    path('post_categoriaa/', post_categoriaa, name="post_categoriaa"),
    path('detalle_categoriaa/<int:id>', updatecategoriaa, name="updatecategoriaa"),
    path('postm_categoriaa/<int:id>', updatecategoriaa, name="postm_categoriaa"),
    path('sacar_datos_categoriaa/<int:id>', updatecategoriaa,name="postm_categoriaa"),
    path('removercategoriaa', removercategoriaa, name='removercategoriaa'),

]