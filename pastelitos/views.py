from django.shortcuts import render
from .forms import *
from .models import *
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login
from django.contrib import messages

def home(request):
    template_to_return='principal.html'
    context={ 
        'view_name': "landing1",
    }
    return render (request,template_to_return,context)


def homep(request):
    template_to_return='landing.html'
    context={ 
        'view_name': "landing1",
    }
    return render (request,template_to_return,context)

##===============PASTEL=====================
def sacar_datos(request, id):
    objeto = pastel.objects.get(id=id)
    id=id
    formulario = pastelform(instance=objeto)
    datos = {'formulario': formulario}
    html_form = render_to_string('updatepastel.html', datos, request=request)
    return HttpResponse(html_form,id)

def removerpastel(request):
    idpastel = request.POST["idpastel"]
    consulta = pastel.objects.get(id=idpastel)
    consulta.delete()
    return HttpResponse('pastel eliminado correctamente')


# Create your views here.
def landing(request):
    template_to_return='hola.html'
    formulario= pastelform()
    consulta = pastel.objects.all()
    context={ 
        'view_name': "landing1",
        'formulario': formulario,
        'consulta': consulta,
    }
    return render (request,template_to_return,context)

def post_pastel(request):
    if request.method=="POST":
        form=pastelform(request.POST,request.FILES)
        if form.is_valid():
            pastel.objects.create(
                cubierta = request.POST["cubierta"],
                precio = request.POST["precio"],
                sabor = request.POST["sabor"],
                peso = request.POST["peso"],
                pisos = request.POST["pisos"],
                tipo = request.POST["tipo"],
            )
            return redirect('landingpastel')
        else:
            form = pastelform()
        return render(request,'hola.html')
    
def updatepastel(request,id):
    resultado=pastel.objects.get(id=id)
    id=id
    form=pastelform(instance=resultado)
    template_to_return = "updatepastel.html"
    if request.method=="POST":
        form=pastelform(request.POST,request.FILES)
        if form.is_valid():
            resultado.cubierta=request.POST["cubierta"]
            resultado.precio=request.POST["precio"]
            resultado.sabor=request.POST["sabor"]
            resultado.peso=request.POST["peso"]
            resultado.pisos=request.POST["pisos"]
            resultado.tipo=request.POST["tipo"]
            resultado.save()
            return redirect("landingpastel")

    context={
        'form':form,
        'resultado':resultado,
        'id':id,
    }
    return render (request, template_to_return,context)

##==============CLIENTES===================
def sacar_datos_cliente(request, id):
    objeto = cliente.objects.get(id=id)
    id=id
    formulario = clienteform(instance=objeto)
    datos = {'formulario': formulario}
    html_form = render_to_string('updatecliente.html', datos, request=request)
    return HttpResponse(html_form,id)

def removercliente(request):
    idcliente = request.POST["idcliente"]
    consulta = cliente.objects.get(id=idcliente)
    consulta.delete()
    return HttpResponse('cliente eliminado correctamente')

# Create your views here.
def landingcliente(request):
    template_to_return='clientes.html'
    formulario= clienteform()
    consulta = cliente.objects.all()
    context={ 
        'view_name': "landing1",
        'formulario': formulario,
        'consulta': consulta,
    }
    return render (request,template_to_return,context)

def post_cliente(request):
    if request.method=="POST":
        form=clienteform(request.POST,request.FILES)
        if form.is_valid():
            num = request.POST["num_int"]
            if num == "":
                num = 0
            cliente.objects.create(
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
            return redirect('landingcliente')
        else:
            form = clienteform()
        return render(request,'clientes.html')
    
def updatecliente(request,id):
    resultado=cliente.objects.get(id=id)
    id=id
    form=clienteform(instance=resultado)
    template_to_return = "updatecliente.html"
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
            return redirect("landingcliente")

    context={
        'form':form,
        'resultado':resultado,
        'id':id,
    }
    return render (request, template_to_return,context)


##==============PROVEEDORES===================
def sacar_datos_proveedor(request, id):
    objeto = proveedor.objects.get(id=id)
    id=id
    formulario = proveedorform(instance=objeto)
    datos = {'formulario': formulario}
    html_form = render_to_string('updateproveedor.html', datos, request=request)
    return HttpResponse(html_form,id)

def removerproveedor(request):
    idproveedor = request.POST["idproveedor"]
    consulta = proveedor.objects.get(id=idproveedor)
    consulta.delete()
    return HttpResponse('proveedor eliminado correctamente')

# Create your views here.
def landingproveedor(request):
    template_to_return='proveedores.html'
    formulario= proveedorform()
    consulta = proveedor.objects.all()
    context={ 
        'view_name': "landing1",
        'formulario': formulario,
        'consulta': consulta,
    }
    return render (request,template_to_return,context)

def post_proveedor(request):
    if request.method=="POST":
        form=proveedorform(request.POST,request.FILES)
        if form.is_valid():
            num = request.POST["num_int"]
            if num == "":
                num = 0
            proveedor.objects.create(
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
            return redirect('landingproveedor')
        else:
            form = proveedorform()
        return render(request,'proveedores.html')
    
def updateproveedor(request,id):
    resultado=proveedor.objects.get(id=id)
    id=id
    form=proveedorform(instance=resultado)
    template_to_return = "updateproveedor.html"
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
            return redirect("landingproveedor")

    context={
        'form':form,
        'resultado':resultado,
        'id':id,
    }
    return render (request, template_to_return,context)


##==============SUCURSALES===================
def sacar_datos_sucursal(request, id):
    objeto = sucursal.objects.get(id=id)
    id=id
    formulario = sucursalform(instance=objeto)
    datos = {'formulario': formulario}
    html_form = render_to_string('updatesucursal.html', datos, request=request)
    return HttpResponse(html_form,id)

def removersucursal(request):
    idsucursal = request.POST["idsucursal"]
    consulta = sucursal.objects.get(id=idsucursal)
    consulta.delete()
    return HttpResponse('sucursal eliminada correctamente')

# Create your views here.
def landingsucursal(request):
    template_to_return='sucursales.html'
    formulario= sucursalform()
    consulta = sucursal.objects.all()
    context={ 
        'view_name': "landing1",
        'formulario': formulario,
        'consulta': consulta,
    }
    return render (request,template_to_return,context)

def post_sucursal(request):
    if request.method=="POST":
        form=sucursalform(request.POST,request.FILES)
        if form.is_valid():
            num = request.POST["num_int"]
            if num == "":
                num = 0
            sucursal.objects.create(
                codigo_postal = request.POST["codigo_postal"],
                calle = request.POST["calle"],
                colonia = request.POST["colonia"],
                num_ext = request.POST["num_ext"],
                num_int = num,
                estado = request.POST["estado"],
                ciudad = request.POST["ciudad"],
                telefono = request.POST["telefono"],
            )
            return redirect('landingsucursal')
        else:
            form = sucursalform()
        return render(request,'sucursales.html')
    
def updatesucursal(request,id):
    resultado=sucursal.objects.get(id=id)
    id=id
    form=sucursalform(instance=resultado)
    template_to_return = "updatesucursal.html"
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
            return redirect("landingsucursal")

    context={
        'form':form,
        'resultado':resultado,
        'id':id,
    }
    return render (request, template_to_return,context)

def practica (request):
    template = "practica.html"
    array = [1,2,3,4,5,6,7,8,9,10]
    print(array)
    context={
        'view_name':"prototipo",
        'array': array,
    }
    return render (request,template,context)


#====================LOGIN====================
def login_usuario(request):
    if request.user.is_authenticated:
        return redirect('pasteles')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('pasteles')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)
    
#======================REGISTRO=================
def registro(request):
    if request.user.is_authenticated:
        return redirect('pasteles')
    else:
        form = CreateUserForm()
        if request.method=='POST':
            form= CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request,'La cuenta ha sido creada para:'+ user)
                return redirect('pasteles')

        context={'form':form}
        return render(request,'register.html',context)
    
from django.shortcuts import render
from django.http import HttpResponse
import re
def greetings(request):
    # var=request.GET['var']
    #res=render(request,'calc.html')
    return render(request, 'calc.html')

def calculation(request):
    if request.method=="POST":
        values=request.POST['values'] #string having whole ques
        print(values)
        vals=re.findall(r"(\d+)",values) #extrect values
        operators=['+','x','÷','-','.','%']
        opr=[]
        for v in values:
            for o in operators:
                if v==o:
                    opr.append(o)
        print(opr)                      #extract operators
        print(re.findall(r"(\d+)",values))

        for o in opr:
            if o=='.':
                i=opr.index(o)
                res=vals[i]+"."+vals[i+1]
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=res
                print(vals)
                print(opr)
        for o in opr:
            if o=='%':
                i=opr.index(o)
                res=(float(vals[i])/100)*float(vals[i+1])
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=res
                print(vals)
                print(opr)
        for o in opr:
            if o=='÷':
                i=opr.index(o)
                res=float(vals[i])/float(vals[i+1])
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=str(res)
                print(vals)
                print(opr)
        for o in opr:
            if o=='x':
                i=opr.index(o)
                res=float(vals[i])*float(vals[i+1])
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=str(res)
                print(vals)
                print(opr)
        for o in opr:
            if o=='+':
                i=opr.index(o)
                res=float(vals[i])+float(vals[i+1])
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=str(res)
                print(vals)
                print(opr)
            if o=='-':
                i=opr.index(o)
                res=float(vals[i])-float(vals[i+1])
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=str(res)
                print(vals)
                print(opr)

        
        # print(opr)
        if len(opr)!=0:
            if opr[0]=='÷':
                result = float(vals[0])/float(vals[1])
            elif opr[0]=='x':
                result = float(vals[0])*float(vals[1])
            elif opr[0]=='+':
                result = float(vals[0])+float(vals[1])
            else :
                result = float(vals[0])-float(vals[1])
        else:
            result = float(vals[0])

        final_result=round(result,2)
        print(final_result)
       


    res=render(request,'calc.html',{'result':final_result,'values':values})
    return res