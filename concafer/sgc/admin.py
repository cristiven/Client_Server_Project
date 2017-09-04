# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Register your models here.
from django.contrib import admin


from .models import Recolector
from .models import Propietario
from .models import AdminCooperativa
from .models import Superusuario
from .models import SuperNumerario

class AdminRecolector(admin.ModelAdmin):
	list_display = ["nombre","ciudad"]
	#para cambiar el enlace 
	#list_display_links = ["ciudad"]
	list_filter = ["ciudad"]
	list_editable = ["ciudad"]
	search_fields = ["nombre","ciudad"]
	class Meta:
		models = Recolector

# Se registra AdminRecolector
admin.site.register(Recolector, AdminRecolector)
admin.site.register(Propietario)
admin.site.register(AdminCooperativa)
admin.site.register(Superusuario)
admin.site.register(SuperNumerario)