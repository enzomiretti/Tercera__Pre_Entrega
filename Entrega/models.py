from django.db import models

# Create your models here.
class Usuarios(models.Model):
    User = models.CharField(max_length=50)
    Mail = models.EmailField(max_length=150)
    Password = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.User} {self.Mail} {self.Password}'

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    stock = models.IntegerField()
    Precio = models.FloatField(default=0)
   
    def __str__(self):
        return f'{self.nombre} {self.stock} {self.Precio}'

class Ventasproducto(models.Model):
    nombreproducto = models.CharField(max_length=50)
    Cantidaddeventas = models.IntegerField()

    def __str__(self):
        return f'{self.nombreproducto} {self.Cantidaddeventas}'



   


