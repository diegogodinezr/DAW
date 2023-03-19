from multiprocessing.sharedctypes import Value
from django import forms
from .models import *

class productoform(forms.ModelForm):
    class Meta:
        model = producto
        fields = '__all__'

class clienteform(forms.ModelForm):
    class Meta:
        model = cliente_a
        fields = '__all__'

class proveedorform(forms.ModelForm):
    class Meta:
        model = proveedor_a
        fields = '__all__'

class sucursalform(forms.ModelForm):
    class Meta:
        model = sucursal_a
        fields = '__all__'

class empleadoform(forms.ModelForm):
    class Meta:
        model = empleado_a
        fields = '__all__'

class categoriaform(forms.ModelForm):
    class Meta:
        model = categoria
        fields = '__all__'