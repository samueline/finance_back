from email.headerregistry import Group
from django.contrib.auth.models import  Group
from rest_framework import viewsets
from rest_framework import permissions
from core.serializers import  GroupSerializer
from django.contrib.auth import authenticate, password_validation

from rest_framework import status,mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from core.models.users import User

from core.serializers.users import UserLoginSerializer, UserModelSerializer, UserSignUpSerializer


class UserViewSet(mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):

    queryset= User.objects.all()
    # serializer_class = UserModelSerializer
    # lookup_field='userid'
    @action(detail=False,methods=['get'])
    def listar(self,request,*args):
        user = User.objects.all()
        # serializer.is_valid(raise_exception=True)
        # user = serializer.save()
        # data = {
        #     'user':UserModelSerializer(user).data,
           
        # }
        # serializer = UserModelSerializer(user,context={'request':request})

        return Response(user,status.HTTP_200_OK)
   
    # permission_classes = [permissions.IsAuthenticated]
    @action(detail=False,methods=['post'])
    def login(self,request):
        serializer_context = {
            'request': request,
        }
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # user = serializer.save()
        # data = {
        #     'user':UserModelSerializer(user).data,
           
        # }
       
            # return data
            # if user is not None:
            #     raise serializers.ValidationError(user)
            
        
            
        # self.context['user'] = user
        # return data
        return Response(serializer.data,status.HTTP_201_CREATED)
    
    serializer_class = UserModelSerializer
    lookup_field = 'id'
    @action(detail=False,methods=['post'])
    def signup(self,request):
        serializer_context = {
            'request': request,
        }
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user,context=serializer_context).data,
           
        return Response(data,status.HTTP_201_CREATED)


class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]    





