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
 
def post_clientea(request):
    if request.method=="POST":
        form=clienteform(request.POST,request.FILES)
        if form.is_valid():
            num = request.POST["num_int"]
            if num == "":
                num = 0
            cliente_a.objects.create(
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
            return redirect('landingclientea')
        else:
            form = clienteform()
        return render(request,'cliente.html')
    
def updateclientea(request,id):
    resultado=cliente_a.objects.get(id=id)
    id=id
    form=clienteform(instance=resultado)
    template_to_return = "updateclientea.html"
    if request.method=="POST":
        form=clienteform(request.POST,request.FILES)
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
            return redirect("landingclientea")

    context={
        'form':form,
        'resultado':resultado,
        'id':id,
    }
    return render (request, template_to_return,context)

def sacar_datos_clientea(request, id):
    objeto = cliente_a.objects.get(id=id)
    id=id
    formulario = clienteform(instance=objeto)
    datos = {'formulario': formulario}
    html_form = render_to_string('updateclientea.html', datos, request=request)
    return HttpResponse(html_form,id)

def removerclientea(request):
    idcliente = request.POST["idcliente"]
    consulta = cliente_a.objects.get(id=idcliente)
    consulta.delete()
    return HttpResponse('Cliente eliminado correctamente')


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
 
def post_proveedora(request):
    if request.method=="POST":
        form=proveedorform(request.POST,request.FILES)
        if form.is_valid():
            num = request.POST["num_int"]
            if num == "":
                num = 0
            proveedor_a.objects.create(
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
            return redirect('landingproveedora')
        else:
            form = proveedorform()
        return render(request,'proveedor.html')
    
def updateproveedora(request,id):
    resultado=proveedor_a.objects.get(id=id)
    id=id
    form=proveedorform(instance=resultado)
    template_to_return = "updateproveedora.html"
    if request.method=="POST":
        form=proveedorform(request.POST,request.FILES)
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
            return redirect("landingproveedora")

    context={
        'form':form,
        'resultado':resultado,
        'id':id,
    }
    return render (request, template_to_return,context)

def sacar_datos_proveedora(request, id):
    objeto = proveedor_a.objects.get(id=id)
    id=id
    formulario = productoform(instance=objeto)
    datos = {'formulario': formulario}
    html_form = render_to_string('updateproveedora.html', datos, request=request)
    return HttpResponse(html_form,id)

def removerproveedora(request):
    idproveedor = request.POST["idproveedor"]
    consulta = proveedor_a.objects.get(id=idproveedor)
    consulta.delete()
    return HttpResponse('Proveedor eliminado correctamente')

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

 
def post_sucursala(request):
    if request.method=="POST":
        form=sucursalform(request.POST,request.FILES)
        if form.is_valid():
            num = request.POST["num_int"]
            if num == "":
                num = 0
            sucursal_a.objects.create(
                codigo_postal = request.POST["codigo_postal"],
                calle = request.POST["calle"],
                colonia = request.POST["colonia"],
                num_ext = request.POST["num_ext"],
                num_int = num,
                estado = request.POST["estado"],
                ciudad = request.POST["ciudad"],
                telefono = request.POST["telefono"],
            )
            return redirect('landingsucursala')
        else:
            form = sucursalform()
        return render(request,'sucursal.html')
    
def updatesucursala(request,id):
    resultado=sucursal_a.objects.get(id=id)
    id=id
    form=sucursalform(instance=resultado)
    template_to_return = "updatesucursala.html"
    if request.method=="POST":
        form=sucursalform(request.POST,request.FILES)
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
            return redirect("landingsucursala")

    context={
        'form':form,
        'resultado':resultado,
        'id':id,
    }
    return render (request, template_to_return,context)

def sacar_datos_sucursala(request, id):
    objeto = sucursal_a.objects.get(id=id)
    id=id
    formulario = sucursalform(instance=objeto)
    datos = {'formulario': formulario}
    html_form = render_to_string('updatesucursala.html', datos, request=request)
    return HttpResponse(html_form,id)

def removersucursala(request):
    idsucursal = request.POST["idsucursal"]
    consulta = sucursal_a.objects.get(id=idsucursal)
    consulta.delete()
    return HttpResponse('Sucursal eliminada correctamente')

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
 
def post_empleadoa(request):
    if request.method=="POST":
        form=empleadoform(request.POST,request.FILES)
        if form.is_valid():
            num = request.POST["num_int"]
            if num == "":
                num = 0
            empleado_a.objects.create(
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
            return redirect('landingempleadoa')
        else:
            form = empleadoform()
        return render(request,'empleado.html')
    
def updateempleadoa(request,id):
    resultado=empleado_a.objects.get(id=id)
    id=id
    form=empleadoform(instance=resultado)
    template_to_return = "updateempleadoa.html"
    if request.method=="POST":
        form=empleadoform(request.POST,request.FILES)
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
            return redirect("landingempleadoa")

    context={
        'form':form,
        'resultado':resultado,
        'id':id,
    }
    return render (request, template_to_return,context)

def sacar_datos_empleadoa(request, id):
    objeto = empleado_a.objects.get(id=id)
    id=id
    formulario = empleadoform(instance=objeto)
    datos = {'formulario': formulario}
    html_form = render_to_string('updateempleadoa.html', datos, request=request)
    return HttpResponse(html_form,id)

def removerempleadoa(request):
    idempleadoa = request.POST["idempleado"]
    consulta = empleado_a.objects.get(id=idempleadoa)
    consulta.delete()
    return HttpResponse('Empleado eliminado correctamente')

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

def post_categoriaa(request):
    if request.method=="POST":
        form=categoriaform(request.POST,request.FILES)
        if form.is_valid():
            categoria.objects.create(
                nombre = request.POST["nombre"],
                descripcion = request.POST["descripcion"]
            )
            return redirect('landingcategoriaa')
        else:
            form = categoriaform()
        return render(request,'categoria.html')
    
def updatecategoriaa(request,id):
    resultado=categoria.objects.get(id=id)
    id=id
    form=categoriaform(instance=resultado)
    template_to_return = "updatecategoriaa.html"
    if request.method=="POST":
        form=categoriaform(request.POST,request.FILES)
        if form.is_valid():
            resultado.nombre = request.POST["nombre"]
            resultado.descripcion = request.POST["descripcion"]
            resultado.save()
            return redirect("landingcategoriaa")

    context={
        'form':form,
        'resultado':resultado,
        'id':id,
    }
    return render (request, template_to_return,context)

def sacar_datos_categoriaa(request, id):
    objeto = categoria.objects.get(id=id)
    id=id
    formulario = categoriaform(instance=objeto)
    datos = {'formulario': formulario}
    html_form = render_to_string('updatecategoriaa.html', datos, request=request)
    return HttpResponse(html_form,id)

def removercategoriaa(request):
    idcategoriaa = request.POST["idcategoria"]
    consulta = categoria.objects.get(id=idcategoriaa)
    consulta.delete()
    return HttpResponse('Categoria eliminada correctamente')
