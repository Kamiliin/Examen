from crypt import methods
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import articulo
from .serializers import articulolistado

# Create your views here.

#@csrf_exempt
@api_view(['GET','POST'])
def lista_articulo(request):
    """
    Lista todos los articulos
    """
    if request.method == 'GET':
        articulo = articulo.objects.all()
        serializer = articulolistado(articulo, many=True)
        return response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = articulolistado(data=data)
        if serializer.is_valid():
            serializer.save()
            return response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)