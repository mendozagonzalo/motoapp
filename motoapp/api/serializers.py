from rest_framework import serializers

from establecimiento.models import Establecimiento
from producto.models import Producto


class EstablecimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Establecimiento
        fields = ['id',
                  'nombre',
                  'direccion',
                  'referencia',
                  'tlf_1',
                  'tlf_2',
                  'tlf_3',
                  'correo',
                  'latitud',
                  'longitud',
                  'distrito',
                  'image',
                  ]


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id',
                  'nombre',
                  'categoria',
                  'marca',
                  'modelo',
                  'descripcion',

                 ]
