from django.http import HttpResponse
from django.shortcuts import render


from django.views.generic import TemplateView

#Para insertar un formulario en una vista se hace esta importacion
from .forms import RegForm

#Se importa del modelo Recolector para poder llenar los datos
from .models import Recolector


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def inicio(request):
	#para saber todo lo que se puede hacer con form
	#print (dir(form))

	#Request.POST es para que el dato que se pida sea obligatorio
	form = RegForm(request.POST or None)
	if form.is_valid():
		form_data = form.cleaned_data
		nom = form_data.get("nombre")
		cda = form_data.get("ciudad")
		obj = Recolector.objects.create(nombre=nom,ciudad=cda)

	#context es un diccionario, el_form es la variable de la plantilla que se va a utilizar dentro del de la plantilla
	context = {
		"el_form": form, 

	}
	return render(request, "inicio.html", context)

