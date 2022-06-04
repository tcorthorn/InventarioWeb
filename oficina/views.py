from django.shortcuts import render

from .models import Proveedor, Destino, Ingreso, Salida
from django.views import generic

def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_ingresos=Ingreso.objects.all().count()
    num_salidas=Salida.objects.all().count()
    num_destinos=Destino.objects.all().count()

    saldo= num_salidas - num_ingresos

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_ingresos':num_ingresos,'num_salidas':num_salidas,'num_destinos':num_destinos, 'saldo':saldo},
    )



class IngresoListView(generic.ListView):
    model = Ingreso

class SalidaListView(generic.ListView):
    model = Salida

class WarecloudsListView(generic.ListView):
    model = Salida
    paginate_by = 10
    queryset = Salida.objects.filter(fecha__icontains="1") 
    template_name = 'Salida/wareclouds_list.html'  # Specify your own template name/location