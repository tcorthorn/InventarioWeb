from django.db import models
from django.forms import CharField, IntegerField
from django.urls import reverse
from datetime import date

class Proveedor(models.Model):
    nombre = models.CharField(max_length=10, default='Otro', null=True, blank=True)
    
    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un proveedor.
        """
        return reverse('detalle-proveedor', args=[str(self.id)])

    class Meta():
        verbose_name='proveedor'
        verbose_name_plural ='Proveedores'

    class Meta():
        ordering =['nombre']

class Destino(models.Model):
    nombre = models.CharField(max_length=100, default='Otro', help_text='Ingrese destino del despacho')
    
    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un proveedor.
        """
        return reverse('detalle-destino', args=[str(self.id)])

    class Meta():
        ordering =['nombre']

class Ingreso(models.Model):
    fecha = models.DateField()
    sku = models.CharField(max_length=7)
    cantidad = models.IntegerField()
    proveedor = models.ManyToManyField(Proveedor) 
    comentario = models.CharField(max_length=200)

    def __str__(self):
        return self.sku

    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un proveedor.
        """
        return reverse('detalle-ingreso', args=[str(self.id)])

    class Meta():
        ordering =['-fecha']

class Salida(models.Model):
    fecha = models.DateField()
    sku = models.CharField(max_length=7)
    cantidad = models.IntegerField()
    destino = models.ManyToManyField(Destino) 
    comentario = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.sku

    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular
        """
        return reverse('detalle-destino', args=[str(self.id)])

    def display_destino(self):

        """"         Creates a string for the cliente. This is required to display destino in Admin.        """

        return ', '.join([ destino.nombre for destino in self.destino.all()[:3] ])
        display_destino.short_description = 'Destino'

    class Meta():
        ordering =['-fecha']


    