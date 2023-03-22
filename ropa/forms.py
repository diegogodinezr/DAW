from multiprocessing.sharedctypes import Value
from django import forms
from .models import *

class productoformr(forms.ModelForm):
    class Meta:
        model = producto_r
        fields = '__all__'

class clienteformr(forms.ModelForm):
    class Meta:
        model = cliente_r
        fields = '__all__'

class proveedorformr(forms.ModelForm):
    class Meta:
        model = proveedor_r
        fields = '__all__'

class sucursalformr(forms.ModelForm):
    class Meta:
        model = sucursal_r
        fields = '__all__'

class empleadoformr(forms.ModelForm):
    class Meta:
        model = empleado_r
        fields = '__all__'

class categoriaformr(forms.ModelForm):
    class Meta:
        model = categoria_r
        fields = '__all__'