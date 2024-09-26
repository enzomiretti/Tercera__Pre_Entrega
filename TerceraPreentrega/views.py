from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from Entrega.forms import ProductoFormulario,UserFormulario,VentasproductoFormulario
from Entrega.models import *
from django.template import Template,Context,loader

def Tienda(req):
    plantilla = loader.get_template("tienda.html")
    documento = plantilla.render()
    return HttpResponse(documento)


def inicio(req):
    plantilla = loader.get_template("Inicio.html")
    documento = plantilla.render()
    return HttpResponse(documento)

def Registro(req):
    print("data",req.POST)
    if req.method == "POST":
        mi_formulario = UserFormulario(req.POST)
        print(mi_formulario)
        
        if mi_formulario.is_valid():
            
            data = mi_formulario.cleaned_data

            nuevo_usuario = Usuarios(User=data["User"],Password=data["Password"],Mail=data["Mail"])

            nuevo_usuario.save()

            return render(req, "inicio.html",{})
        else:
            return render(req,"registro.html",{"mi_formulario" : mi_formulario})
            
    else:
        mi_formulario = UserFormulario()
        return render(req,"registro.html",{"mi_formulario" : mi_formulario})
    
def Stock(req):
    print("data",req.POST)
    if req.method == "POST":
        form_stock = ProductoFormulario(req.POST)
        print(form_stock)
        
        if form_stock.is_valid():
            
            data = form_stock.cleaned_data

            Nuevo_producto = Producto(nombre=data["nombre"],stock=data["stock"],Precio=data["Precio"])

            Nuevo_producto.save()

            return render(req, "inicio.html",{})
        else:
            return render(req,"tienda.html",{"form_stock" : form_stock})
            
    else:
        form_stock = ProductoFormulario()
        return render(req,"stock.html",{"form_stock" : form_stock})
    

def Ventas(req):
    print("data",req.POST)
    if req.method == "POST":
        form_sales = VentasproductoFormulario(req.POST)
        print(form_sales)
        
        if form_sales.is_valid():
            
            data = form_sales.cleaned_data

            nueva_venta = Ventasproducto(nombreproducto=data["nombreproducto"],Cantidaddeventas=data["Cantidaddeventas"])

            nueva_venta.save()

            return render(req, "inicio.html",{})
        else:
            return render(req,"ventas.html",{"form_sales" : form_sales})
            
    else:
        form_sales = VentasproductoFormulario()
        return render(req,"ventas.html",{"form_sales" : form_sales})


