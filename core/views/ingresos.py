
from logging import raiseExceptions
from core.models.gastos import Gastos
from core.models.total import Total
from core.serializers import IngresoModelSerializer,AddIngresoModel,UpdateIngresoModel
from rest_framework import mixins, viewsets

from django.http import Http404, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import Ingreso
from rest_framework import mixins
from rest_framework import generics
from rest_framework.decorators import action
import datetime 
import numpy as np

from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

from core.serializers.gastos import GastosModelSerializer

class IngresosViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    # viewsets.ModelViewSet):
    # mixins.ListModelMixin,
    #               mixins.CreateModelMixin,
    #               generics.GenericAPIView):
    queryset = Ingreso.objects.all()
    serializer_class = IngresoModelSerializer
    @action(detail=True,methods=['get'])
    def listar(self,  *args,**kwargs):

        dti = datetime.datetime.today()
        # start = datetime.date(dti.year, dti.month, 01)
        st = datetime.date(dti.year, dti.month,1)
        end = datetime.date(dti.year, dti.month,30)

        ingreso = Ingreso.objects.filter(created__gte=st).filter(created__lte=end)
        # ingreso = Ingreso.objects.all()
        # ingreso = "hoa"
        # serializer_class = IngresoModelSerializer
        serializer = IngresoModelSerializer(ingreso,many=True)
        # print(ingreso)
        # return ingreso
        
        return Response(serializer.data)

    # @action(detail=True,methods=['post'])
    def crear(self, request, *args, **kwargs):
        # ingreso = Ingreso.objects.all()
     
        ingreso = AddIngresoModel.create(self,data=request.data)
        
        if ingreso == True:
            return Response(status=status.HTTP_201_CREATED)
        return Response(ingreso.errors, status=status.HTTP_400_BAD_REQUEST)


    queryset = Ingreso.objects.all()
    serializer_class = IngresoModelSerializer
    lookup_field = 'id'
    def actualizar(self, request, *args, **kwargs):
        # ingreso = Ingreso.objects.all()
        instance = get_object_or_404(Ingreso, id = request.data.get("id"))
    

        serializer = self.get_serializer(instance,data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


    queryset = Total.objects.all()
    

    def porcentajes(self,  *args,**kwargs):
        ahorro = 0
        ingres = 0
        gasto = 0

        dti = datetime.datetime.today()
        # start = datetime.date(dti.year, dti.month, 01)
        st = datetime.date(dti.year, dti.month,1)
        end = datetime.date(dti.year, dti.month,30)
        gastos = Gastos.objects.filter(created__gte=st).filter(created__lte=end)
        ingreso = Ingreso.objects.filter(created__gte=st).filter(created__lte=end)
        serializer = IngresoModelSerializer(ingreso,many=True)
        for ing in serializer.data:
            ingreso= float(ing['valor'])
            ingres = ingreso + ingres

        serializer_gasto = GastosModelSerializer(gastos,many=True)
        for gas in serializer_gasto.data:
            gastos= float(gas['valor'])
            gasto = gastos + gasto

        total = ingres - gasto
        ahorro = ingres * 0.3
        gastos_ahorro = total - ahorro

       
        ahorro_a = Total.objects.all()
        aho = 0
        if len(ahorro_a) != 0:
            
            
            for a in ahorro_a.data:
                
                ah = float(a['ahorro'])
                
                aho += ah

            aho = aho + ahorro
     
        respuesta = {'total':total,'ahorro':int(ahorro), 'gastos':int(gastos_ahorro),'ahorro_anual':aho}

        # instance = get_object_or_404(Total,)
    

        # serializers =  CreateTotalModel.createe(self,data=respuesta)
        # if serializers == True:
        #     return Response(respuesta,status=status.HTTP_201_CREATED)
        # return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        # crear base de datos que guarde el ahorro mensual y muestre el total ahorrado, se puede retirar todo el ahorro o parte
        # hacer barra para agregar tareas crud
        return Response(respuesta)
        total =  ingreso - gastos

        ahorro = ingreso  * 0.1
        return total

    def retirar_ahorro(self,request,*args):
        instance = get_object_or_404(Total, id = request.data.get("id"))

        serializer = self.get_serializer(instance,data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

        # serializer.is_valid(raise_exception=True)
        # self.perform_update(serializer)

        # return Response(serializer.data)


         




    