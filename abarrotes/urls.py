from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from abarrotes.views import *
from .views import *

urlpatterns = [
    url(r'^$',landinga, name="landinga"),

    url('landingproductoa/',landingproductoa, name="landingproductoaa"),

    url('landingclientea/',landingclientea, name="landingclientea"),

    url('landingproveedora/',landingproveedora, name="landingproveedora"),
    
    url('landingsucursala/',landingsucursala, name="landingsucursala"),

    url('landingempleadoa/',landingempleadoa, name="landingempleadoa"),

    url('landingcategoriaa/',landingcategoriaa, name="landingcategoriaa"),
]