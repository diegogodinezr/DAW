from django.shortcuts import render
#from .forms import *
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
