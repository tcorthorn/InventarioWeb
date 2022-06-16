from django.contrib import admin
from .models import Proveedor, Sku, Ingreso, Salida
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from datetime import date

class InventResource(resources.ModelResource):
    class Meta:
        model = Proveedor
        model =Sku
        model = Ingreso
        model = Salida
     
@admin.register(Proveedor)
class ProveedorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('nombre',)
    list_filter = ('nombre',)
    resources_class = Proveedor
    search_fields = ("nombre", )
    
@admin.register(Sku)
class SkuAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('creado','codigo', 'categoria','producto')
    list_filter = ('categoria',)
    resources_class = Sku
    search_fields = ("categoria", )

@admin.register(Ingreso)
class IngresoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('creado','sku','cantidad', 'comentario')
    list_filter = ('sku', 'creado')
    resources_class = Ingreso
    search_fields = ("sku", )

@admin.register(Salida)
class SalidaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('creado', 'sku', 'cantidad', 'destino', 'comentario')
    list_filter = ( 'creado', 'destino','sku')
    resources_class = Salida
    search_fields = ("destino",  )