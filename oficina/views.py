from django.shortcuts import render
from django.db.models import Avg, Sum
from .models import Proveedor, Ingreso, Salida, Sku, Inventario_oficina
from django.views import generic
from django.db.models import Count, F
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


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

    # Renderiza la plantilla
    return render(
        request,
        'index.html',
        context={'num_ingresos':num_ingresos,'num_salidas':num_salidas,'salidas_totales':salidas_totales, 'ingresos_totales':ingresos_totales, 'stock':stock},
    )

class SkuListView(generic.ListView):
    model = Sku
    paginate_by = 15

class IngresoListView(generic.ListView):
    model = Ingreso
    paginate_by = 10

class SalidaListView(generic.ListView):
    model = Salida
    paginate_by = 10

class Inventario_oficinaListView(generic.ListView):
    model = Inventario_oficina
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


#Formulario para buscar sku

def busqueda_productos(request):
    return render (request, "formulario.html")
 
def buscar(request):
    if request.GET["cod"]:

        producto=request.GET["cod"]

        if len(producto) == 7 :

            num_ingresos=Ingreso.objects.all().filter(sku__codigo=producto)
            num_salidas = Salida.objects.all().filter(sku__codigo=producto)

            ingresos_totales=sum(num_ingresos.values_list('cantidad',flat=True))
            salidas_totales=sum(num_salidas.values_list('cantidad',flat=True))

            stock= ingresos_totales - salidas_totales

            prod_list =Sku.objects.filter(codigo=producto)

            # Renderiza la plantilla
            return render(request, 'busca.html', context={'salidas_totales':salidas_totales, 'ingresos_totales':ingresos_totales, 'stock':stock, "query":producto, 'prod_list':prod_list})   

        else:
            mensaje= " Código SKU debe tener 7 dígitos"

            return render(request, 'busca.html', context={'mensaje':mensaje, "query":producto}) 
          
    else:
            
            mensaje= "No has ingresado datos"
            return render(request, 'busca.html', context={'mensaje':mensaje}) 


 # Búsqueda de stock por productos

def todos(request):

    cod_list =Ingreso.objects.order_by('sku__codigo').distinct('sku__codigo')
    ing=Ingreso.objects.values('sku__codigo').order_by('sku__codigo').annotate(suma=Sum('cantidad'))
    
    cod_salid =Salida.objects.order_by('sku__codigo').distinct('sku__codigo')
    sal=Salida.objects.values('sku__codigo').order_by('sku__codigo').annotate(suma=Sum('cantidad'))

    union= ing.union(sal,all=True)

    list=[]
    for producto in cod_list:
    
        num_ingresos=Ingreso.objects.all().filter(sku__codigo=producto.sku)
        num_salidas = Salida.objects.all().filter(sku__codigo=producto.sku)

        ingresos_totales=sum(num_ingresos.values_list('cantidad',flat=True))
        salidas_totales=sum(num_salidas.values_list('cantidad',flat=True))

        stock= ingresos_totales - salidas_totales

        list =list.append(stock)

        prod_list =Sku.objects.filter(codigo=producto.sku)

        # Renderiza la plantilla
        return render(request, 'todos.html', 
                context={'salidas_totales':salidas_totales, 'ingresos_totales':ingresos_totales, 
                'stock':stock, "query":producto, 'prod_list':prod_list,
                'cod_list':cod_list,'list':list, 'ing':ing,'cod_salid':cod_salid,'sal':sal,'union':union})   

   


# Formularios para ingresar; modificar y eliminar

class SkuCreate(CreateView):
    model = Sku
    fields = '__all__'
    
class SkuUpdate(UpdateView):
    model = Sku
    fields = fields = '__all__'

class SkuDelete(DeleteView):
    model = Sku
    success_url =fields = '__all__'


class IngresoCreate(CreateView):
    model = Ingreso
    fields = '__all__'
    
class IngresoUpdate(UpdateView):
    model = Ingreso
    fields = fields = '__all__'

class IngresoDelete(DeleteView):
    model = Ingreso
    success_url =fields = '__all__'


class SalidaCreate(CreateView):
    model = Salida
    fields = '__all__'
    
class SalidaUpdate(UpdateView):
    model = Salida
    fields = fields = '__all__'

class SalidaDelete(DeleteView):
    model = Salida
    success_url =fields = '__all__'

#Busca el stock de todos los productos en Oficina

 

        
          
   

        
   