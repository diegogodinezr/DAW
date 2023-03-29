from multiprocessing.sharedctypes import Value
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']