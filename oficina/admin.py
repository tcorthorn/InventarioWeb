from django.contrib import admin
from .models import Proveedor, Catalogo, Ingreso, Salida
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from datetime import date

class InventResource(resources.ModelResource):
    class Meta:
        model = Proveedor
        model =Catalogo
        model = Ingreso
        model = Salida
     
@admin.register(Proveedor)
class ProveedorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('nombre',)
    list_filter = ('nombre',)
    resources_class = Proveedor
    search_fields = ("nombre", )
    
@admin.register(Catalogo)
class CatalogoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('creado','sku', 'categoria','producto')
    list_filter = ('categoria',)
    resources_class = Catalogo
    search_fields = ("categoria", )

@admin.register(Ingreso)
class IngresoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('creado','display_sku','cantidad', 'comentario')
    list_filter = ('sku', 'creado')
    resources_class = Ingreso
    search_fields = ("sku", )

@admin.register(Salida)
class SalidaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('creado', 'display_sku', 'cantidad', 'destino', 'comentario')
    list_filter = ( 'creado', 'destino','sku')
    resources_class = Salida
    search_fields = ("destino",  )