import django_filters

from producto.models import Producto


class ProductoFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    precio_final = django_filters.NumberFilter
    precio_final__gt = django_filters.NumberFilter(name='precio_final', lookup_expr='gt')
    precio_final__lt = django_filters.NumberFilter(name='precio_final', lookup_expr='lt')

    class Meta:
        model = Producto
        fields = ['marca', 'precio_final']