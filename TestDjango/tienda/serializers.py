from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from core.models import articulo

class articulolistado(serializers.modelsSerializer):
    class meta:
        model = articulo
        fields =['nombre','codigo','precio']