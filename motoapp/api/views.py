import django_filters.rest_framework
from geopy.distance import great_circle
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.response import Response

from api.filter import ProductoFilter
from api.serializers import EstablecimientoSerializer, ProductoSerializer
from establecimiento.models import Establecimiento
from producto.models import Producto


class EstablecimientoListView(ListAPIView):
    queryset = Establecimiento.objects.all()
    serializer_class = EstablecimientoSerializer

    def get_queryset(self):
        qs = self.queryset.all()

        lat = float(self.kwargs.get('latitud'))
        lon = float(self.kwargs.get('longitud'))

        establecimientos_cercanos = []
        for q in qs:
            distancia = calcular_distancia(float(lat), float(lon), float(q.latitud), float(q.longitud))
            #Distancia en kM
            #Mejora:Que sea dinámico
            if distancia < 8:
                establecimientos_cercanos.append(q)
        return establecimientos_cercanos


class ProductoListView(ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = ProductoFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if queryset.count() > 0:
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response({"status": status.HTTP_200_OK,
                             "data": serializer.data},
                            status=status.HTTP_200_OK)
        else:
            return Response({"status": status.HTTP_204_NO_CONTENT},
                            status=status.HTTP_204_NO_CONTENT)


def calcular_distancia(lat1, lon1, lat2, lon2):
    coord_base = (lat1, lon1)
    coord_estbl = (lat2, lon2)
    dist = great_circle(coord_base, coord_estbl).km
    return dist
