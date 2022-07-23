from django.shortcuts import render
from django.db.models import Avg, Sum
from .models import Proveedor, Ingreso, Salida, Sku, Inventario_oficina, Inventario_aura, Inventario_casa_moda
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

    stock= ingresos_totales + salidas_totales

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

class PackcoListView(generic.ListView):
    model = Salida
    paginate_by = 10
    queryset = Salida.objects.all().filter(destino__icontains="Packco") 
    template_name = 'oficina/packco_list.html'  # Specify your own template name/location

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


class Inventario_auraListView(generic.ListView):
    model = Inventario_aura
    paginate_by = 10

class Inventario_casa_modaListView(generic.ListView):
    model = Inventario_casa_moda
    paginate_by = 10

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

            stock= ingresos_totales + salidas_totales

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

        # Renderiza la plantilla

    return render(request, 'todos.html', context={'cod_list':cod_list,'ing':ing,'cod_salid':cod_salid,'sal':sal})   

   
def ingreso_por_producto(request):

    cod_list =Ingreso.objects.order_by('sku__codigo').distinct('sku__codigo')
    ing=Ingreso.objects.values('sku__codigo').order_by('sku__codigo').annotate(suma=Sum('cantidad'))
    
    cod_salid =Salida.objects.order_by('sku__codigo').distinct('sku__codigo')
    sal=Salida.objects.values('sku__codigo').order_by('sku__codigo').annotate(suma=Sum('cantidad'))


        
        # Renderiza la plantilla

    return render(request, 'ingreso_por_producto.html', context={"ing":ing})   



# Formularios para ingresar; modificar y eliminar

class SkuCreate(CreateView):
    model = Sku
    fields = '__all__'
    success_url = reverse_lazy('skus')

class SkuUpdate(UpdateView):
    model = Sku
    fields = '__all__'
    success_url = reverse_lazy('skus')

class SkuDelete(DeleteView):
    model = Sku
    success_url = reverse_lazy('skus')


class IngresoCreate(CreateView):
    model = Ingreso
    fields = '__all__'
    success_url = reverse_lazy('ingresos')
    
class IngresoUpdate(UpdateView):
    model = Ingreso
    fields = '__all__'
    success_url = reverse_lazy('ingresos')

class IngresoDelete(DeleteView):
    model = Ingreso
    success_url = reverse_lazy('ingresos')


class SalidaCreate(CreateView):
    model = Salida
    fields = '__all__'
    success_url = reverse_lazy('salidas')

class SalidaUpdate(UpdateView):
    model = Salida
    fields = fields = '__all__'
    success_url = reverse_lazy('salidas')

class SalidaDelete(DeleteView):
    model = Salida
    success_url = reverse_lazy('salidas')

#Busca el stock instantáneo de todos los productos en Oficina

def total(request):

    cod_list =Ingreso.objects.order_by('sku__codigo').distinct('sku__codigo')
    ing=Ingreso.objects.values('sku__codigo').order_by('sku__codigo').annotate(suma=Sum('cantidad'))

    
    cod_salid =Salida.objects.order_by('sku__codigo').distinct('sku__codigo')
    sal=Salida.objects.values('sku__codigo').order_by('sku__codigo').annotate(suma=Sum('cantidad' ))

    total = ing.union(ing,sal).order_by('sku__codigo')



        # Renderiza la plantilla

    return render(request, 'total.html', context={'total':total}) 

        
          
   

        
   