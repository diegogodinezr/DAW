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
 
def post_productoa(request):
    if request.method=="POST":
        form=productoform(request.POST,request.FILES)
        if form.is_valid():
            producto.objects.create(
                nombre = request.POST["nombre"],
                precio = request.POST["precio"],
                categoria = request.POST["categoria"],
                cantidad = request.POST["cantidad"],
                tipo = request.POST["tipo"],
            )
            return redirect('landingproductoa')
        else:
            form = productoform()
        return render(request,'producto.html')
    
def updateproductoa(request,id):
    resultado=producto.objects.get(id=id)
    id=id
    form=productoform(instance=resultado)
    template_to_return = "updateproducto.html"
    if request.method=="POST":
        form=productoform(request.POST,request.FILES)
        if form.is_valid():
            resultado.nombre = request.POST["nombre"]
            resultado.precio = request.POST["precio"]
            resultado.categoria = request.POST["categoria"]
            resultado.cantidad = request.POST["cantidad"]
            resultado.tipo = request.POST["tipo"]
            resultado.save()
            return redirect("landingproductoa")

    context={
        'form':form,
        'resultado':resultado,
        'id':id,
    }
    return render (request, template_to_return,context)

def sacar_datos_productoa(request, id):
    objeto = producto.objects.get(id=id)
    id=id
    formulario = productoform(instance=objeto)
    datos = {'formulario': formulario}
    html_form = render_to_string('updateproducto.html', datos, request=request)
    return HttpResponse(html_form,id)

def removerproductoa(request):
    idproducto = request.POST["idproducto"]
    consulta = producto.objects.get(id=idproducto)
    consulta.delete()
    return HttpResponse('producto eliminado correctamente')

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