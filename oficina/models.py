from tabnanny import verbose
from django.db import models
from django.forms import CharField, IntegerField
from django.urls import reverse
from datetime import date

class Proveedor(models.Model):
    creado= models.DateField(auto_now_add=True)
    nombre = models.CharField(max_length=10, default='Otro', null=True, blank=True)
    comentario = models.CharField(max_length=200, null=True,blank=True )
    
 
    
    def __str__(self):
        return self.nombre
    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un proveedor.
        """
        return reverse('detalle-proveedor', args=[str(self.id)])

    class Meta:
        verbose_name = 'proveedor'
        verbose_name_plural = 'proveedores'

    class Meta():
        ordering =['nombre']

class Sku(models.Model):
    creado= models.DateField(auto_now_add=True)
    codigo = models.CharField(max_length = 7, unique = True )
    categoria = models.CharField(max_length=20) 
    producto = models.CharField(max_length=100) 
    proveedor = models.ForeignKey(Proveedor,  on_delete=models.SET_NULL, null= True)
    comentario = models.CharField(max_length=200, null=True,blank=True )
    
    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name ="sku"
        verbose_name_plural = "sku"
    
    class Meta:
        ordering =['categoria', 'producto']

    def get_absolute_url(self):
        """         Devuelve el URL a una instancia particular de Catalogo         """
        return reverse('detalle-sku', args=[str(self.id)])

class Ingreso(models.Model):
    creado= models.DateField(auto_now_add=True)
    sku = models.ManyToManyField(Sku)
    cantidad = models.IntegerField()
    proveedor = models.ManyToManyField(Proveedor) 
    comentario = models.CharField(max_length=200, null=True,blank=True , default='Comentario')

    def __str__(self):
        return self.comentario

    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un proveedor.
        """
        return reverse('detalle-ingreso', args=[str(self.id)])
    class Meta:
        ordering =['-creado']

    def display_sku(self):
        """"         Creates a string for the cliente. This is required to display sku in Admin.        """

        return ', '.join([ sku.sku for sku in self.sku.all()[:3] ])
    display_sku.short_description = 'SKU'


class Salida(models.Model):
    creado= models.DateField(auto_now_add=True)
    sku = models.ManyToManyField(Sku)
    cantidad = models.IntegerField()
    LOAN_DESTINO = (
        ('wareclouds', 'Wareclouds'),
        ('casamoda','CasaModa'),
        ('aura','Aura'),
        ('enviodirecto','EnvioDirecto'),
        ('otro','Otro'),
    )
    destino = models.CharField(max_length=20 , choices=LOAN_DESTINO , blank=True)
    comentario = models.CharField(max_length=300 , null=True , blank=True)
  
    def __str__(self):
        return self.destino

    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular
        """
        return reverse('detalle-salida', args=[str(self.id)])

    def display_sku(self):
        """"         Creates a string for the cliente. This is required to display sku in Admin.        """

        return ', '.join([ sku.sku for sku in self.sku.all()[:3] ])
        
    display_sku.short_description = 'SKU'

    class Meta():
        ordering =['-creado']


    