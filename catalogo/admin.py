from django.contrib import admin
from .models import Propiedad

class PropiedadAdmin(admin.ModelAdmin):
    list_display = ('fecha_publicacion','descripcion','direccion', 'usuario', 'precio', 'area', 'num_habitaciones', 'num_baños')
    search_fields = ('direccion', 'usuario__username')  # Buscar por dirección y nombre de usuario
    list_filter = ('usuario',)  # Filtrar por usuario

admin.site.register(Propiedad, PropiedadAdmin)