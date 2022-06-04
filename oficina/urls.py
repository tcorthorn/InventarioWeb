
from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name ='index'),
   path('ingresos/', views.IngresoListView.as_view(), name ='ingresos'),
   path('salidas/', views.SalidaListView.as_view(), name ='salidas'),

   path('wareclouds/', views.WarecloudsListView.as_view(), name='wareclouds'),

]