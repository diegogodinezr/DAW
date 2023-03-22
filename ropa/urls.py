from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from ropa.views import *
from .views import *

urlpatterns = [
    url(r'^$',landingr, name="landingr"),

]