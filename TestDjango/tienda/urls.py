from django.urls import URLPattern, path
from tienda.views import lista_articulo

URLPatterns = [
    path('lista_articulo',lista_articulo, name="lista_articulo")
]