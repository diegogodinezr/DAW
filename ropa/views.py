from django.shortcuts import render
from .forms import *
from .models import *
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template.loader import render_to_string


# Create your views here.
#=================VISTA GENERAL====================
def landingr(request):
    template_to_return='ropa.html'
    context={ 
        'view_name': "landing1",
    }
    return render (request,template_to_return,context)

#=================PRODUCTO====================
def landingproductor(request):
    template_to_return='productor.html'
    formulario= productoformr()
    consulta = producto_r.objects.all()
    context={ 
        'view_name': "landing1",
        'formulario': formulario,
        'consulta': consulta,
    }
    return render (request,template_to_return,context)
 
def post_productor(request):
    if request.method=="POST":
        form=productoformr(request.POST,request.FILES)
        if form.is_valid():
            producto_r.objects.create(
                nombre = request.POST["nombre"],
                precio = request.POST["precio"],
                categoria = request.POST["categoria"],
                cantidad = request.POST["cantidad"],
                tipo = request.POST["tipo"],
            )
            return redirect('landingproductor')
        else:
            form = productoformr()
        return render(request,'productor.html')
    
def updateproductor(request,id):
    resultado=producto_r.objects.get(id=id)
    id=id
    form=productoformr(instance=resultado)
    template_to_return = "updateproductor.html"
    if request.method=="POST":
        form=productoformr(request.POST,request.FILES)
        if form.is_valid():
            resultado.nombre = request.POST["nombre"]
            resultado.precio = request.POST["precio"]
            resultado.categoria = request.POST["categoria"]
            resultado.cantidad = request.POST["cantidad"]
            resultado.tipo = request.POST["tipo"]
            resultado.save()
            return redirect("landingproductor")

    context={
        'form':form,
        'resultado':resultado,
        'id':id,
    }
    return render (request, template_to_return,context)

def sacar_datos_productor(request, id):
    objeto = producto_r.objects.get(id=id)
    id=id
    formulario = productoformr(instance=objeto)
    datos = {'formulario': formulario}
    html_form = render_to_string('updateproductor.html', datos, request=request)
    return HttpResponse(html_form,id)

def removerproductor(request):
    idproductor = request.POST["idproducto"]
    consulta = producto_r.objects.get(id=idproductor)
    consulta.delete()
    return HttpResponse('producto eliminado correctamente')

#=================CLIENTE====================
def landingclienter(request):
    template_to_return='clienter.html'
    formulario= clienteformr()
    consulta = cliente_r.objects.all()
    context={ 
        'view_name': "landing1",
        'formulario': formulario,
        'consulta': consulta,
    }
    return render (request,template_to_return,context)
 
def post_clienter(request):
    if request.method=="POST":
        form=clienteformr(request.POST,request.FILES)
        if form.is_valid():
            num = request.POST["num_int"]
            if num == "":
                num = 0
            cliente_r.objects.create(
                nombre = request.POST["nombre"],
                apellido = request.POST["apellido"],
                codigo_postal = request.POST["codigo_postal"],
                calle = request.POST["calle"],
                colonia = request.POST["colonia"],
                num_ext = request.POST["num_ext"],
                num_int = num,
                estado = request.POST["estado"],
                ciudad = request.POST["ciudad"],
            )
            return redirect('landingclienter')
        else:
            form = clienteformr()
        return render(request,'clienter.html')
    
def updateclienter(request,id):
    resultado=cliente_r.objects.get(id=id)
    id=id
    form=clienteformr(instance=resultado)
    template_to_return = "updateclienter.html"
    if request.method=="POST":
        form=clienteformr(request.POST,request.FILES)
        if form.is_valid():
            num = request.POST["num_int"]
            if num == "":
                num = 0
            resultado.nombre = request.POST["nombre"]
            resultado.apellido = request.POST["apellido"]
            resultado.codigo_postal = request.POST["codigo_postal"]
            resultado.calle = request.POST["calle"]
            resultado.colonia = request.POST["colonia"]
            resultado.num_ext = request.POST["num_ext"]
            resultado.num_int = num
            resultado.estado = request.POST["estado"]
            resultado.ciudad = request.POST["ciudad"]
            resultado.save()
            return redirect("landingclienter")

    context={
        'form':form,
        'resultado':resultado,
        'id':id,
    }
    return render (request, template_to_return,context)

def sacar_datos_clienter(request, id):
    objeto = cliente_r.objects.get(id=id)
    id=id
    formulario = clienteformr(instance=objeto)
    datos = {'formulario': formulario}
    html_form = render_to_string('updateclienter.html', datos, request=request)
    return HttpResponse(html_form,id)

def removerclienter(request):
    idclienter = request.POST["idcliente"]
    consulta = cliente_r.objects.get(id=idclienter)
    consulta.delete()
    return HttpResponse('Cliente eliminado correctamente')


#=================PROVEEDOR====================
def landingproveedorr(request):
    template_to_return='proveedorr.html'
    formulario= proveedorformr()
    consulta = proveedor_r.objects.all()
    context={ 
        'view_name': "landing1",
        'formulario': formulario,
        'consulta': consulta,
    }
    return render (request,template_to_return,context)
 
def post_proveedorr(request):
    if request.method=="POST":
        form=proveedorformr(request.POST,request.FILES)
        if form.is_valid():
            num = request.POST["num_int"]
            if num == "":
                num = 0
            proveedor_r.objects.create(
                empresa = request.POST["empresa"],
                codigo_postal = request.POST["codigo_postal"],
                calle = request.POST["calle"],
                colonia = request.POST["colonia"],
                num_ext = request.POST["num_ext"],
                num_int = num,
                estado = request.POST["estado"],
                ciudad = request.POST["ciudad"],
                telefono = request.POST["telefono"],
            )
            return redirect('landingproveedorr')
        else:
            form = proveedorformr()
        return render(request,'proveedorr.html')
    
def updateproveedorr(request,id):
    resultado=proveedor_r.objects.get(id=id)
    id=id
    form=proveedorformr(instance=resultado)
    template_to_return = "updateproveedorr.html"
    if request.method=="POST":
        form=proveedorformr(request.POST,request.FILES)
        if form.is_valid():
            num = request.POST["num_int"]
            if num == "":
                num = 0
            resultado.empresa = request.POST["empresa"]
            resultado.codigo_postal = request.POST["codigo_postal"]
            resultado.calle = request.POST["calle"]
            resultado.colonia = request.POST["colonia"]
            resultado.num_ext = request.POST["num_ext"]
            resultado.num_int = num
            resultado.estado = request.POST["estado"]
            resultado.ciudad = request.POST["ciudad"]
            resultado.telefono = request.POST["telefono"]
            resultado.save()
            return redirect("landingproveedorr")

    context={
        'form':form,
        'resultado':resultado,
        'id':id,
    }
    return render (request, template_to_return,context)

def sacar_datos_proveedorr(request, id):
    objeto = proveedor_r.objects.get(id=id)
    id=id
    formulario = productoformr(instance=objeto)
    datos = {'formulario': formulario}
    html_form = render_to_string('updateproveedorr.html', datos, request=request)
    return HttpResponse(html_form,id)

def removerproveedorr(request):
    idproveedorr = request.POST["idproveedor"]
    consulta = proveedor_r.objects.get(id=idproveedorr)
    consulta.delete()
    return HttpResponse('Proveedor eliminado correctamente')

#=================SUCURSAL====================
def landingsucursalr(request):
    template_to_return='sucursalr.html'
    formulario= sucursalformr()
    consulta = sucursal_r.objects.all()
    context={ 
        'view_name': "landing1",
        'formulario': formulario,
        'consulta': consulta,
    }
    return render (request,template_to_return,context)

 
def post_sucursalr(request):
    if request.method=="POST":
        form=sucursalformr(request.POST,request.FILES)
        if form.is_valid():
            num = request.POST["num_int"]
            if num == "":
                num = 0
            sucursal_r.objects.create(
                codigo_postal = request.POST["codigo_postal"],
                calle = request.POST["calle"],
                colonia = request.POST["colonia"],
                num_ext = request.POST["num_ext"],
                num_int = num,
                estado = request.POST["estado"],
                ciudad = request.POST["ciudad"],
                telefono = request.POST["telefono"],
            )
            return redirect('landingsucursalr')
        else:
            form = sucursalformr()
        return render(request,'sucursalr.html')
    
def updatesucursalr(request,id):
    resultado=sucursal_r.objects.get(id=id)
    id=id
    form=sucursalformr(instance=resultado)
    template_to_return = "updatesucursalr.html"
    if request.method=="POST":
        form=sucursalformr(request.POST,request.FILES)
        if form.is_valid():
            num = request.POST["num_int"]
            if num == "":
                num = 0
            resultado.codigo_postal = request.POST["codigo_postal"]
            resultado.calle = request.POST["calle"]
            resultado.colonia = request.POST["colonia"]
            resultado.num_ext = request.POST["num_ext"]
            resultado.num_int = num
            resultado.estado = request.POST["estado"]
            resultado.ciudad = request.POST["ciudad"]
            resultado.telefono = request.POST["telefono"]
            resultado.save()
            return redirect("landingsucursalr")

    context={
        'form':form,
        'resultado':resultado,
        'id':id,
    }
    return render (request, template_to_return,context)

def sacar_datos_sucursalr(request, id):
    objeto = sucursal_r.objects.get(id=id)
    id=id
    formulario = sucursalformr(instance=objeto)
    datos = {'formulario': formulario}
    html_form = render_to_string('updatesucursalr.html', datos, request=request)
    return HttpResponse(html_form,id)

def removersucursalr(request):
    idsucursalr = request.POST["idsucursal"]
    consulta = sucursal_r.objects.get(id=idsucursalr)
    consulta.delete()
    return HttpResponse('Sucursal eliminada correctamente')

#=================EMPLEADO====================
def landingempleador(request):
    template_to_return='empleador.html'
    formulario= empleadoformr()
    consulta = empleado_r.objects.all()
    context={ 
        'view_name': "landing1",
        'formulario': formulario,
        'consulta': consulta,
    }
    return render (request,template_to_return,context)
 
def post_empleador(request):
    if request.method=="POST":
        form=empleadoformr(request.POST,request.FILES)
        if form.is_valid():
            num = request.POST["num_int"]
            if num == "":
                num = 0
            empleado_r.objects.create(
                nombre = request.POST["nombre"],
                apellido = request.POST["apellido"],
                codigo_postal = request.POST["codigo_postal"],
                calle = request.POST["calle"],
                colonia = request.POST["colonia"],
                num_ext = request.POST["num_ext"],
                num_int = num,
                estado = request.POST["estado"],
                ciudad = request.POST["ciudad"],
            )
            return redirect('landingempleador')
        else:
            form = empleadoformr()
        return render(request,'empleador.html')
    
def updateempleador(request,id):
    resultado=empleado_r.objects.get(id=id)
    id=id
    form=empleadoformr(instance=resultado)
    template_to_return = "updateempleador.html"
    if request.method=="POST":
        form=empleadoformr(request.POST,request.FILES)
        if form.is_valid():
            num = request.POST["num_int"]
            if num == "":
                num = 0
            resultado.nombre = request.POST["nombre"]
            resultado.apellido = request.POST["apellido"]
            resultado.codigo_postal = request.POST["codigo_postal"]
            resultado.calle = request.POST["calle"]
            resultado.colonia = request.POST["colonia"]
            resultado.num_ext = request.POST["num_ext"]
            resultado.num_int = num
            resultado.estado = request.POST["estado"]
            resultado.ciudad = request.POST["ciudad"]
            resultado.save()
            return redirect("landingempleador")

    context={
        'form':form,
        'resultado':resultado,
        'id':id,
    }
    return render (request, template_to_return,context)

def sacar_datos_empleador(request, id):
    objeto = empleado_r.objects.get(id=id)
    id=id
    formulario = empleadoformr(instance=objeto)
    datos = {'formulario': formulario}
    html_form = render_to_string('updateempleador.html', datos, request=request)
    return HttpResponse(html_form,id)

def removerempleador(request):
    idempleador = request.POST["idempleado"]
    consulta = empleado_r.objects.get(id=idempleador)
    consulta.delete()
    return HttpResponse('Empleado eliminado correctamente')

#=================CATEGORIA====================
def landingcategoriar(request):
    template_to_return='categoriar.html'
    formulario= categoriaformr()
    consulta = categoria_r.objects.all()
    context={ 
        'view_name': "landing1",
        'formulario': formulario,
        'consulta': consulta,
    }
    return render (request,template_to_return,context)

def post_categoriar(request):
    if request.method=="POST":
        form=categoriaformr(request.POST,request.FILES)
        if form.is_valid():
            categoria_r.objects.create(
                nombre = request.POST["nombre"],
                descripcion = request.POST["descripcion"]
            )
            return redirect('landingcategoriar')
        else:
            form = categoriaformr()
        return render(request,'categoriar.html')
    
def updatecategoriar(request,id):
    resultado=categoria_r.objects.get(id=id)
    id=id
    form=categoriaformr(instance=resultado)
    template_to_return = "updatecategoriar.html"
    if request.method=="POST":
        form=categoriaformr(request.POST,request.FILES)
        if form.is_valid():
            resultado.nombre = request.POST["nombre"]
            resultado.descripcion = request.POST["descripcion"]
            resultado.save()
            return redirect("landingcategoriar")

    context={
        'form':form,
        'resultado':resultado,
        'id':id,
    }
    return render (request, template_to_return,context)

def sacar_datos_categoriar(request, id):
    objeto = categoria_r.objects.get(id=id)
    id=id
    formulario = categoriaformr(instance=objeto)
    datos = {'formulario': formulario}
    html_form = render_to_string('updatecategoriar.html', datos, request=request)
    return HttpResponse(html_form,id)

def removercategoriar(request):
    idcategoriar = request.POST["idcategoria"]
    consulta = categoria_r.objects.get(id=idcategoriar)
    consulta.delete()
    return HttpResponse('Categoria eliminada correctamente')
