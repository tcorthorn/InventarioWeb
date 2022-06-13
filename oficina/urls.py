
from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name ='index'),

   path('ingresos/', views.IngresoListView.as_view(), name ='ingresos'),
   path('salidas/', views.SalidaListView.as_view(), name ='salidas'),
   path('skus/', views.SkuListView.as_view(), name ='skus'),

   path('ingreso/<pk>', views.IngresoDetailView.as_view(), name='detalle-ingreso'),
   path('salida/<pk>', views.SalidaDetailView.as_view(), name='detalle-salida'),
   path('sku/<pk>', views.SkuDetailView.as_view(), name='detalle-sku'),


   path('wareclouds/', views.WarecloudsListView.as_view(), name='wareclouds'),
   path('casamoda/', views.CasamodaListView.as_view(), name='casamoda'),
   path('aura/', views.AuraListView.as_view(), name='aura'),
   path('directo/', views.DirectoListView.as_view(), name='directo'),
   path('otro/', views.OtroListView.as_view(), name='otro'),

   ]