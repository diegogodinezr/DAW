from multiprocessing.sharedctypes import Value
from urllib import request
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import *

class pastelform(forms.ModelForm):
    class Meta:
        model = pastel
        fields = '__all__'

class clienteform(forms.ModelForm):
    class Meta:
        model = cliente
        fields = '__all__'

class proveedorform(forms.ModelForm):
    class Meta:
        model = proveedor
        fields = '__all__'

class sucursalform(forms.ModelForm):
    class Meta:
        model = sucursal
        fields = '__all__'