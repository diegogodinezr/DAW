from django.shortcuts import render
from .forms import *
from .models import *
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template.loader import render_to_string


# Create your views here.
#=================VISTA GENERAL====================
def landinga(request):
    template_to_return='abarrotes.html'
    context={ 
        'view_name': "landing1",
    }
    return render (request,template_to_return,context)

#=================PRODUCTO====================
def landingproductoa(request):
    template_to_return='producto.html'
    formulario= productoform()
    consulta = producto.objects.all()
    context={ 
        'view_name': "landing1",
        'formulario': formulario,
        'consulta': consulta,
    }
    return render (request,template_to_return,context)

#=================CLIENTE====================
def landingclientea(request):
    template_to_return='cliente.html'
    formulario= clienteform()
    consulta = cliente_a.objects.all()
    context={ 
        'view_name': "landing1",
        'formulario': formulario,
        'consulta': consulta,
    }
    return render (request,template_to_return,context)

#=================PROVEEDOR====================
def landingproveedora(request):
    template_to_return='proveedor.html'
    formulario= proveedorform()
    consulta = proveedor_a.objects.all()
    context={ 
        'view_name': "landing1",
        'formulario': formulario,
        'consulta': consulta,
    }
    return render (request,template_to_return,context)

#=================SUCURSAL====================
def landingsucursala(request):
    template_to_return='sucursal.html'
    formulario= sucursalform()
    consulta = sucursal_a.objects.all()
    context={ 
        'view_name': "landing1",
        'formulario': formulario,
        'consulta': consulta,
    }
    return render (request,template_to_return,context)

#=================EMPLEADO====================
def landingempleadoa(request):
    template_to_return='empleado.html'
    formulario= empleadoform()
    consulta = empleado_a.objects.all()
    context={ 
        'view_name': "landing1",
        'formulario': formulario,
        'consulta': consulta,
    }
    return render (request,template_to_return,context)
#=================CATEGORIA====================
def landingcategoriaa(request):
    template_to_return='categoria.html'
    formulario= categoriaform()
    consulta = categoria.objects.all()
    context={ 
        'view_name': "landing1",
        'formulario': formulario,
        'consulta': consulta,
    }
    return render (request,template_to_return,context)