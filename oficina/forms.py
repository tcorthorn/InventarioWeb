
from django import forms
from django.core.exceptions import ValidationError
import datetime #for checking renewal date range.




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


