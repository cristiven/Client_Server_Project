from django.http import HttpResponse
from django.shortcuts import render

#Para insertar un formulario en una vista se hace esta importacion
from .forms import RegForm

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def inicio(request):
	form = RegForm()
	#context es un diccionario, el_form es la variable de la plantilla que se va a utilizar dentro del de la plantilla

	context = {
		"el_form": form, 

	}
	return render(request, "inicio.html", context)

