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

    url('landingproveedora/',landingproveedora, name="landingproveedora"),
    
    url('landingsucursala/',landingsucursala, name="landingsucursala"),

    url('landingempleadoa/',landingempleadoa, name="landingempleadoa"),

    url('landingcategoriaa/',landingcategoriaa, name="landingcategoriaa"),
]