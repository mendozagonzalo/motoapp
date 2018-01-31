from django.db import models

from producto.models import Producto


class Venta(models.Model):

    RESERVADO = 'r'
    PAGADO = 'p'
    ENVIADO = 'e'
    CANCELADO = 'c'

    ESTADO_VENTA_CHOICES = (
        (RESERVADO, 'RESERVADO'),
        (PAGADO, 'PAGADO'),
        (ENVIADO, 'ENVIADO'),
        (CANCELADO, 'CANCELADO')
    )

    fecha_pedido = models.DateTimeField(auto_now_add=True)
    fecha_pagado = models.DateTimeField(null=True, blank=True)
    fecha_enviado = models.DateTimeField(null=True, blank=True)
    productos = models.ManyToManyField(Producto, related_name='venta', through='VentaProducto')
    #user = models.ForeignKey(User, related_name='sales')
    total_acumulado = models.FloatField(verbose_name='Monto total', null=True, blank=True)
    #voucher = models.FileField(upload_to='sales/vouchers', null=True, blank=True)
    #code_voucher = models.CharField(max_length=200, null=True, blank=True)
    estado = models.CharField(max_length=1, choices=ESTADO_VENTA_CHOICES, default=RESERVADO)


class VentaProducto(models.Model):
    fecha_registro = models.DateTimeField(auto_now_add=True)
    venta = models.ForeignKey(Venta, related_name='venta_productos')
    producto = models.ForeignKey(Producto, related_name='venta_productos')
    cantidad = models.PositiveIntegerField()
    #size = models.CharField(max_length=3, blank=True, null=True)
    parcial_acumulado = models.FloatField()

