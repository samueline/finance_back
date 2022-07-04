from django.shortcuts import get_object_or_404
from rest_framework import viewsets,mixins
from core import serializers
from core.models import Gastos
from core.serializers import GastosModelSerializer, addGastosModelSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from core.serializers.gastos import addGastosModelSerializer

class GastoViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                         mixins.UpdateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):

    queryset = Gastos.objects.all()
    serializer_class = GastosModelSerializer
    


    @action(detail=True,methods=['get'])
    def listar(self,  *args,**kwargs):
        gasto = Gastos.objects.all()
        # ingreso = "hoa"
        # serializer_class = IngresoModelSerializer
        serializer = GastosModelSerializer(gasto)
        # print(ingreso)
        # return ingreso
        
        return Response(serializer.data)
        # def listar(self,request,  *args,**kwargs):
    def crear(self, request, *args, **kwargs):
        # ingreso = Ingreso.objects.all()
     
        gastos = addGastosModelSerializer.create(self,data=request.data)
        # serializer_class = 
        # print(ingreso)
        # if ingreso:
        # ingreso.save()
        # 
        if gastos == True:
            return Response(status=status.HTTP_201_CREATED)
        return Response(gastos.errors, status=status.HTTP_400_BAD_REQUEST)
        #     gastos = Gastos.objects.all()
        #     serializer = GastosModelSerializer(gastos)
        #     return serializer

    queryset = Gastos.objects.all()
    serializer_class = GastosModelSerializer
    lookup_field = 'id'
    def actualizar(self, request, *args, **kwargs):
        # ingreso = Ingreso.objects.all()
        instance = get_object_or_404(Gastos, id = request.data.get("id"))
    

        serializer = self.get_serializer(instance,data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

