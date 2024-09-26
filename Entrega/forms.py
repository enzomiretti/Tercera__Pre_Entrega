from django import forms

class UserFormulario(forms.Form):

    User = forms.CharField(required=True)
    Password = forms.CharField(required=True)
    Mail = forms.CharField(required=True)

class ProductoFormulario(forms.Form):

    nombre = forms.CharField(required=True)
    stock = forms.IntegerField(required=True)
    Precio = forms.FloatField(required=True)

class VentasproductoFormulario(forms.Form):
    nombreproducto = forms.CharField(required=True)
    Cantidaddeventas = forms.IntegerField(required=True)