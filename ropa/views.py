from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your views here.
def hola(request):
    template=loader.get_template('ropa.html')
    context={
        'vista':'vista2',
        'app':'app 2',
    }
    return HttpResponse(template.render(context,request))