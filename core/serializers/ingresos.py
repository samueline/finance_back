from datetime import datetime
from rest_framework import serializers

from core.models import Ingreso
from core.models.total import Total

class IngresoModelSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Ingreso
        fields = [
            'name','descripcion'
            ,'valor','activo',
            'id','created'
        ]
        # read_only_fields = [ 
        #     'name',
        #     'descripcion',
        #     'valor',
        #     'activo'
        # ]


class AddIngresoModel(serializers.Serializer):

    def create(self,data):
        
        user = Ingreso.objects.create(
            name= data['name'],
            descripcion=data['descripcion'],
            valor=data['valor'],
            # si esta activo 1
            # created=datetime.now()
            activo=1

        )
        return True

class UpdateIngresoModel(serializers.Serializer):
    def update(self,data,validate):
        user = Ingreso.objects.create(
            name= data['name'],
            descripcion=data['descripcion'],
            valor=data['valor'],
            # si esta activo 1
            # created=datetime.now()
            activo=1

        )
        return True



