from django.db import models

# Create your models here.
class  pastel(models.Model):
    cubierta = models.CharField(max_length=20, blank=False, default=None)
    precio = models.FloatField(blank=False, default=None)
    sabor = models.CharField(max_length=40, blank=False, default=None)
    peso = models.FloatField(blank=False, default=None)
    pisos = models.IntegerField(null=False, blank=False)
    tipo = models.CharField(max_length=40, blank=False, default=None)

class cliente(models.Model):
    nombre = models.CharField(max_length=20, blank=False, default=None)
    apellido = models.CharField(max_length=70, blank=False, default=None)
    codigo_postal = models.IntegerField(null=False, blank=False)
    calle = models.CharField(max_length=100, blank=False, default=None)
    colonia = models.CharField(max_length=100, blank=False, default=None)
    num_ext = models.IntegerField(null=False, blank=False)
    num_int = models.IntegerField(null=False, blank=False)
    estado = models.CharField(max_length=20, blank=False, default=None)
    ciudad = models.CharField(max_length=50, blank=False, default=None)

class proveedor(models.Model):
    empresa = models.CharField(max_length=70, blank=False, default=None)
    codigo_postal = models.IntegerField(null=False, blank=False)
    calle = models.CharField(max_length=100, blank=False, default=None)
    colonia = models.CharField(max_length=100, blank=False, default=None)
    num_ext = models.IntegerField(null=False, blank=False)
    num_int = models.IntegerField(null=False, blank=False)
    estado = models.CharField(max_length=20, blank=False, default=None)
    ciudad = models.CharField(max_length=50, blank=False, default=None)
    telefono = models.IntegerField(null=False, blank=False)

class sucursal(models.Model):
    codigo_postal = models.IntegerField(null=False, blank=False)
    calle = models.CharField(max_length=100, blank=False, default=None)
    colonia = models.CharField(max_length=100, blank=False, default=None)
    num_ext = models.IntegerField(null=False, blank=False)
    num_int = models.IntegerField(null=False, blank=False)
    estado = models.CharField(max_length=20, blank=False, default=None)
    ciudad = models.CharField(max_length=50, blank=False, default=None)
    telefono = models.IntegerField(null=False, blank=False)
