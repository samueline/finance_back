
from core.models import Tareas
from core.serializers import IngresoModelSerializer,AddTareaModel,UpdateTareaModel,DeleteTareaModel
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
import pytz

from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

from core.serializers.tareas import TareaModelSerializer

class TareasViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    # viewsets.ModelViewSet):
    # mixins.ListModelMixin,
    #               mixins.CreateModelMixin,
    #               generics.GenericAPIView):
    queryset = Tareas.objects.all()
    serializer_class = TareaModelSerializer
    @action(detail=True,methods=['get'])
    def listar(self,  *args,**kwargs):

        # dti = datetime.datetime.today()
       
        # st = datetime.datetime(dti.year, dti.month,1)
        # end = datetime.datetime(dti.year, dti.month,30)

        tarea = Tareas.objects.filter(activo=1)
      
        serializer = TareaModelSerializer(tarea,many=True)
        
        
        return Response(serializer.data)

    # @action(detail=True,methods=['post'])
    def create(self, request, *args, **kwargs):
        # ingreso = Ingreso.objects.all()
        # return Response(True)
        ingreso = AddTareaModel.create(self,data=request.data)
        # return Response(ingreso)
        if ingreso == True:
            return Response(status=status.HTTP_201_CREATED)
        return Response(ingreso.errors, status=status.HTTP_400_BAD_REQUEST)


    # queryset = Ingreso.objects.all()
    # serializer_class = IngresoModelSerializer
    lookup_field = 'id'
    @action(detail=True,methods=['put'])

    def actualizar(self, request, *args, **kwargs):
        # ingreso = Ingreso.objects.all()
        instance = get_object_or_404(Tareas, id = request.data.get("id"))
    

        serializer = self.get_serializer(instance,data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


    # @action(detail=True,methods=['delete'])

    def eliminar(self,request,pk,format=None):
        # tarea=self.get_object(pk)
        # return Response(pk)
        serializer = DeleteTareaModel.eliminar(self,pk)
        return Response(serializer,status=status.HTTP_204_NO_CONTENT)
        # def delete(self, request, pk, format=None):
        # event = self.get_object(pk)
        # event.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT



    