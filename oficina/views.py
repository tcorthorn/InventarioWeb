from django.shortcuts import render
from django.db.models import Avg, Sum
from .models import Proveedor, Ingreso, Salida
from django.views import generic
from django.db.models import Count, F
def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales

    num_ingresos=Ingreso.objects.all().count()
    total_ingresos=Ingreso.objects.all().aggregate(Total_productos_ingresados = Sum('cantidad'))

    num_salidas=Salida.objects.all().count()
    total_salidas = Salida.objects.all().aggregate(Total_productos_enviados = Sum('cantidad'))

    sku = Salida.objects.filter(sku="1").aggregate(Sum('cantidad'))

    uno =Salida.sku
   
   
    # Renderiza la plantilla
    return render(
        request,
        'index.html',
        context={'num_ingresos':num_ingresos,'num_salidas':num_salidas,'total_ingresos':total_ingresos,'total_salidas':total_salidas, 'sku': sku,'uno':uno},
    )



class IngresoListView(generic.ListView):
    model = Ingreso
    paginate_by = 10

class SalidaListView(generic.ListView):
    model = Salida
    paginate_by = 10

class WarecloudsListView(generic.ListView):
    model = Salida
    paginate_by = 10
    queryset = Salida.objects.all().filter(destino__icontains="WareClouds") 
    template_name = 'oficina/wareclouds_list.html'  # Specify your own template name/location

class CasamodaListView(generic.ListView):
    model = Salida
    paginate_by = 10
    queryset = Salida.objects.all().filter(destino__icontains="CasaModa") 
    template_name = 'oficina/casamoda_list.html'  # Specify your own template name/location    

class AuraListView(generic.ListView):
    model = Salida
    paginate_by = 10
    queryset = Salida.objects.all().filter(destino__icontains="Aura") 
    template_name = 'oficina/aura_list.html'  # Specify your own template name/location 

class DirectoListView(generic.ListView):
    model = Salida
    paginate_by = 10
    queryset = Salida.objects.all().filter(destino__icontains="EnvioDirecto") 
    template_name = 'oficina/directo_list.html'  # Specify your own template name/location 

class OtroListView(generic.ListView):
    model = Salida
    paginate_by = 10
    queryset = Salida.objects.all().filter(destino__icontains="Otro") 
    template_name = 'oficina/otro_list.html'  # Specify your own template name/location 
