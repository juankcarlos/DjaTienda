from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from decimal import Decimal
from datetime import datetime

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, blank=True)
    descripcion = models.TextField()


class Producto(models.Model):
    nombre = models.CharField(max_length=10, blank=True)
    docfile = models.FileField(upload_to='documents', blank=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2,
                        default=Decimal(0.00))
    descripcion = models.TextField(blank=True)
    categorias = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Factura(models.Model):
    fecha = models.DateTimeField(default=datetime.now(), blank=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE)


class DetallesVenta(models.Model):
    facturas = models.ForeignKey(Factura, on_delete=models.CASCADE)
    productos = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
