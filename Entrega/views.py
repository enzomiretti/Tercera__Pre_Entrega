from django.http import HttpResponse
from .models import Usuarios
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context,loader
from django.urls import path



def Tienda(req):
    plantilla = loader.get_template("tienda.html")
    documento = plantilla.render()
    return HttpResponse(documento)


def inicio(req):
    plantilla = loader.get_template("Inicio.html")
    documento = plantilla.render()
    return HttpResponse(documento)



def buscarusuario(req):
    return render(req, "buscar_usuario.html")

def buscar(req):
    usuarioo =req.GET["User"]
    usuario = Usuarios.objects.filter(User__icontains=usuarioo)

    return render(req,"resultado_busqueda.html",{"Users" : usuario })
