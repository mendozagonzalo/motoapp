from django.contrib import admin

from producto.models import Producto, Imagen, Marca, Modelo


class ImageInline(admin.TabularInline):
    model = Imagen
    extra = 0
    verbose_name = 'Imagen'
    verbose_name_plural = 'Imagenes'

class ProductoAdmin(admin.ModelAdmin):
    model = Producto
    readonly_fields = ('precio_final')
    fields = (
               'nombre',
               'categoria',
               'marca',
               'modelo',
               'descripcion',
               'tipo_moneda',
               'precio_bruto',
               'descuento',
               'precio_final',
               'fecha_registro',
               'imagen_principal',
               'stock',
               'establecimientos',
            )

    inlines = (ImageInline,)
    readonly_fields = ('fecha_registro',)

admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Imagen)
