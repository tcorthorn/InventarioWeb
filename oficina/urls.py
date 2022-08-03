
from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name ='index'),

   path('ingresos/', views.IngresoListView.as_view(), name ='ingresos'),
   path('salidas/', views.SalidaListView.as_view(), name ='salidas'),
   path('skus/', views.SkuListView.as_view(), name ='skus'),
   path('inv/', views.Inventario_oficinaListView.as_view(), name ='inv'),
   path('inv_aura/', views.Inventario_auraListView.as_view(), name ='inv_aura'),
   path('inv_moda/', views.Inventario_casa_modaListView.as_view(), name ='inv_moda'),

   path('ingreso/<pk>', views.IngresoDetailView.as_view(), name='detalle-ingreso'),
   path('salida/<pk>', views.SalidaDetailView.as_view(), name='detalle-salida'),
   path('sku/<pk>', views.SkuDetailView.as_view(), name='detalle-sku'),

   path('packco/', views.PackcoListView.as_view(), name='packco'),
   path('casamoda/', views.CasamodaListView.as_view(), name='casamoda'),
   path('aura/', views.AuraListView.as_view(), name='aura'),
   path('directo/', views.DirectoListView.as_view(), name='directo'),
   path('otro/', views.OtroListView.as_view(), name='otro'),

   path('busqueda_productos/', views.busqueda_productos, name='busqueda'),
   path('todos/', views.todos, name='todos'),
   path('ing_prod/', views.ingreso_por_producto, name ='ing_prod'),
   path('total/', views.total, name ='total'),

   path('cod/create/', views.SkuCreate.as_view(), name='sku_create'),
   path('cod/<pk>/update/', views.SkuUpdate.as_view(), name='sku_update'),
   path('cod/<pk>/delete/', views.SkuDelete.as_view(), name='sku_delete'),

   path('ing/create/', views.IngresoCreate.as_view(), name='ingreso_create'),
   path('ing/<pk>/update/', views.IngresoUpdate.as_view(), name='ingreso_update'),
   path('ing/<pk>/delete/', views.IngresoDelete.as_view(), name='ingresodelete'),

   path('sal/create/', views.SalidaCreate.as_view(), name='salida_create'),
   path('sal/<pk>/update/', views.SalidaUpdate.as_view(), name='salida_update'),
   path('sal/<pk>/delete/', views.SalidaDelete.as_view(), name='salida_delete'),

   ]