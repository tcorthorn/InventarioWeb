
from django import forms
from django.core.exceptions import ValidationError
import datetime #for checking renewal date range.
from django.forms import ModelForm
from .models import Sku, Ingreso, Salida

class SaldoForm(forms.Form): 
    cod = forms.CharField(help_text= "Entre el SKU buscado")

    def clean_cod(self):
        data = self.cleaned_data['cod']

         #Check date.
        if len(data) > 7 : 
            raise ValidationError('Sku debe ser de 7 digitos')
        else: 
            if len(data) < 7 :
                raise ValidationError('Sku debe ser de 7 digitos')

        return data

class SkuModelForm(ModelForm):

    def clean_cod(self):
        data = self.cleaned_cod['codigo']

         #Check date.
        if len(data) != 7 : 
            raise ValidationError('Sku debe ser de 7 digitos')
        return data

    class Meta:
        model = Sku
        fields = '__all__'

class IngresoModelForm(ModelForm):

    def clean_cod(self):
        data = self.cleaned_cod['sku']

         #Check date.
        if len(data) != 7 : 
            raise ValidationError('Sku debe ser de 7 digitos')
        return data

    class Meta:
        model = Ingreso
        fields = '__all__'

class SalidaModelForm(ModelForm):

    def clean_cod(self):
        data = self.cleaned_cod['sku']

         #Check date.
        if len(data) != 7 : 
            raise ValidationError('Sku debe ser de 7 digitos')
        return data

    class Meta:
        model = Salida
        fields = '__all__'