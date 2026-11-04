from django.contrib import admin
from .models import CategoriaFaena, Maquinaria

@admin.register(CategoriaFaena)
class CategoriaFaenaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'creado_en')
    search_fields = ('nombre',)

@admin.register(Maquinaria)
class MaquinariaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'categoria', 'precio_arriendo_dia', 'stock', 'estado', 'destacado')
    list_filter = ('categoria', 'estado', 'tipo_oferta', 'destacado')
    search_fields = ('codigo', 'nombre', 'descripcion')
    list_editable = ('precio_arriendo_dia', 'stock', 'estado', 'destacado')