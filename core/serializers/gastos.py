from rest_framework import serializers
from core.models import Gastos

class GastosModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gastos
        fields=[
             'name','descripcion'
            ,'valor','activo',
            'id','created'
        ]

class addGastosModelSerializer(serializers.Serializer):
    def create(self,data):
        user = Gastos.objects.create(
            name= data['name'],
            descripcion=data['descripcion'],
            valor=data['valor'],
            # si esta activo 1
            activo=1

            )
        return True
