from django.urls import path
from TerceraPreentrega.views import inicio,Stock,Registro,Ventas
from Entrega.views import buscarusuario,buscar

urlpatterns = [
    
    path('', inicio,name="Inicio"),
    path('stock/', Stock,name="stock"),
    path('register/', Registro,name="Register"),
    path('ventas/', Ventas,name="Ventas"),
    path('busqueda-usuario/',buscarusuario,name="busqueda" ),
    path('buscar/',buscar,name="buscar"),


]
