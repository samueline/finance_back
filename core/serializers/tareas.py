from datetime import datetime
from pytz import timezone
from rest_framework import serializers
from core.models import Tareas


class TareaModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tareas
        fields=['descripcion','activo','fecha_ejecucion','titulo','created','id']



class AddTareaModel(serializers.Serializer):

    def create(self,data):
        
        user = Tareas.objects.create(
            titulo=data['titulo'],
            descripcion=data['descripcion'],
            # titulo = data['titulo'],
            created=datetime.now(),
            fecha_ejecucion=data['fecha_ejecucion'],
            # ,
            activo=1

        )
        return True

class UpdateTareaModel(serializers.Serializer):
    def update(self,data,validate):
        # user = (
        #     descripcion=data['descripcion'],
            

        # )
        return True

class DeleteTareaModel(serializers.Serializer):
    def eliminar(self,pk):

        usuario = Tareas.objects.get(id=pk)
        # return usuario
        usuario.activo = 0
        usuario.save()
        return True




