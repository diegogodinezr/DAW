from django.shortcuts import render
from .forms import *
from .models import *
from django.shortcuts import redirect

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
            print(form)
            pastel.objects.create(
                cubierta = request.POST["cubierta"],
                precio = request.POST["precio"],
                sabor = request.POST["sabor"],
                peso = request.POST["peso"],
                pisos = request.POST["pisos"],
                tipo = request.POST["tipo"],
            )
            return redirect('landing')
        else:
            form = pastelform()
        return render(request,'hola.html',context)
    
def updatepastel (request, id):
    resultado = pastel.objects.get(id = id)
    print (id)
    id=id
    form = pastelform(instance=resultado)
    template_to_return = "updatepastel.html"
    if request.method=="POST":
        form=pastelform(request.POST,request.FILES)
        if form.is_valid():
            resultado.cubierta = request.POST["cubierta"]
            resultado.precio = request.POST["precio"]
            resultado.sabor = request.POST["sabor"]
            resultado.peso = request.POST["peso"]
            resultado.pisos = request.POST["pisos"]
            resultado.tipo = request.POST["tipo"]
            resultado.save()
            return redirect("landing")

    context = {
        'form': form,
        'resultado': resultado,
        'id':id,
    }
    return render (request, template_to_return, context)