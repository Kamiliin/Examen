from mailbox import NoSuchMailboxError
from turtle import title
from django.db import models

# Create your models here.


class carrito(models.Model):
    nombre=models.CharField(max_length=100)
    categoria=models.CharField(max_length=50)
    precio=models.IntegerField()

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'


class cliente (models.Model):
    primer_nombre=models.CharField(max_length=30)
    segundo_nombre=models.CharField(max_length=30)
    rut=models.CharField(max_length=9)
    sexo=models.BooleanField()
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
    telefono=models.CharField(max_length=7)
    contraseña=models.CharField(max_length=50)

class articulo(models.Model):
    nombre_articulo=models.CharField(max_length=30)
    codigo=models.CharField(max_length=20)
    precio=models.IntegerField()

class tipo_articulo(models.Model):
    nombre_tipo=models.CharField(max_length=50)   

"""    
class pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()    
"""