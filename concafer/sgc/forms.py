from django import forms


#Se crea el formulario con los campos que se quiera, ya que es diferente 
#al de los modelos y se puede añadir a una vista
class RegForm(forms.Form):
	nombre = forms.CharField(max_length=20)
	ciudad = forms.CharField(max_length=20)