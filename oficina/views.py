from django.shortcuts import render
from django.db.models import Avg, Sum
from .models import Proveedor, Ingreso, Salida, Sku
from django.views import generic
from django.db.models import Count, F
def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales

    num_ingresos=Ingreso.objects.all().count()
    num_salidas=Salida.objects.all().count()

    ingresos=Ingreso.objects.all()
    ingresos_totales=sum(ingresos.values_list('cantidad',flat=True))

    salidas=Salida.objects.all()
    salidas_totales=sum(salidas.values_list('cantidad',flat=True))

    stock= ingresos_totales - salidas_totales
    
    # total_ingresos=Ingreso.objects.all().aggregate(Total_ingresados = Sum('cantidad'))
    # total_salidas = Salida.objects.all().aggregate(Total_productos_enviados = Sum('cantidad'))

   
   
   
    # Renderiza la plantilla
    return render(
        request,
        'index.html',
        context={'num_ingresos':num_ingresos,'num_salidas':num_salidas,'salidas_totales':salidas_totales, 'ingresos_totales':ingresos_totales, 'stock':stock},
    )

class SkuListView(generic.ListView):
    model = Sku
    paginate_by = 10

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




# Detalle de la Clase

class IngresoDetailView(generic.DetailView):
    model = Ingreso
    paginate_by = 10

class SalidaDetailView(generic.DetailView):
    model = Salida
    paginate_by = 10

class SkuDetailView(generic.DetailView):
    model = Sku
    paginate_by = 10