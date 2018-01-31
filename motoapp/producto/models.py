from django.db import models

from easy_thumbnails.fields import ThumbnailerImageField

from establecimiento.models import Establecimiento
from motoclick.utils.mixins import UidMixin


class Marca(models.Model):
    nombre = models.CharField(verbose_name='Marca', max_length=100)
    codigo= models.CharField(verbose_name='Codigo', max_length=50)
    imagen = models.ImageField(upload_to='images/marca', verbose_name='Imagen Marca', blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.nombre)


class Modelo(models.Model):
    nombre = models.CharField(verbose_name='Modelo', max_length=200, null=True, blank=True)
    codigo= models.CharField(verbose_name='Codigo', max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='modelo_marcas')

    def __str__(self):
        return '{}'.format(self.nombre)


class Producto(UidMixin, models.Model):
    USD = "usd"
    PEN = "pen"

    ACCESORIO = 'A'
    REPUESTO = 'R'

    CATEGORIA_CHOICES = (
        (ACCESORIO, 'ACCESORIO'),
        (REPUESTO, 'REPUESTO'),
    )

    nombre = models.CharField(verbose_name='Producto', max_length=300, blank=True, null=True)
    categoria = models.CharField(max_length=1, choices=CATEGORIA_CHOICES, default=ACCESORIO)
    marca = models.ForeignKey(Marca, related_name='producto_marcas', null=True, blank=True)
    modelo = models.ForeignKey(Modelo, related_name='producto_modelos', null=True, blank=True)
    descripcion = models.TextField(verbose_name='Descripción general', blank=True, null=True)
    tipo_moneda = models.CharField(verbose_name='Tipo de Moneda', max_length=3,
                                   choices=((USD, "Dólares"), (PEN, "Soles")), blank=True, null=True, )
    precio_bruto = models.FloatField(verbose_name='Precio Bruto')
    descuento = models.PositiveIntegerField(verbose_name='Descuento', help_text='15%,30%, etc', blank=True, null=True)
    precio_final = models.FloatField(verbose_name='Precio con descuento', blank=True, null=True)
    fecha_registro = models.DateTimeField(verbose_name='Fecha de Registro', auto_now_add=True)
    imagen_principal = ThumbnailerImageField(upload_to='productos/images', null=True,
                                             verbose_name='Imagen principal del producto')
    stock = models.PositiveIntegerField(default=1, verbose_name='Stock')
    establecimientos = models.ManyToManyField(Establecimiento, related_name='productos', blank=True)

    def __unicode__(self):
        return '{}'.format(self.nombre)

    def save(self, *args, **kwargs):
        try:
            if self.descuento:
                self.precio_final = self.precio_bruto - round((self.precio_bruto * self.descuento) / 100, 2)
            else:
                self.precio_final = self.precio_bruto
        except Exception:
            pass
        super(Producto, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.nombre)


class Imagen(models.Model):
    photo = ThumbnailerImageField(upload_to='productos/images', verbose_name='Fotos del producto')
    # is_enabled = models.BooleanField(default=True)
    producto = models.ForeignKey(Producto, related_name='images', verbose_name='Producto', null=True)

    def __str__(self):
        return '{}'.format(self.photo.url)
