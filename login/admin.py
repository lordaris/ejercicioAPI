from django.contrib import admin
import rutinas.models as rutinas_models

# Register your models here.

admin.site.register(rutinas_models.Rutina)
admin.site.register(rutinas_models.Dia)
admin.site.register(rutinas_models.Ejercicio)
