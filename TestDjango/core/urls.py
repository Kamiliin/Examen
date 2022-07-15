from django.urls import path
from .views import inicio, bandanas, identificadores, accesorios, correas, registro, conocenosMejor

urlpatterns = [
    path('', inicio,name="inicio"),
    path('bandanas.html/', bandanas,name="bandanas"),
    path('identificadores.html/', identificadores,name="identificadores"),
    path('accesorios.html/', accesorios,name="accesorios"),
    path('correas.html/', correas,name="correas"),
    path('registro.html/', registro,name="registro"),
    path('conocenosMejor.html/', conocenosMejor,name="conocenosMejor"),

]