from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^establecimientos/(?P<latitud>-?\d+.\d+)/(?P<longitud>-?\d+.\d+)', views.EstablecimientoListView.as_view()),
    url(r'^productos/$', views.ProductoListView.as_view())
]
