import re
from django.contrib.auth.models import  Group
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from django.contrib.auth import authenticate, password_validation
from core.models.users import User

class UserModelSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['id','username','email']



class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Group
        fields = ['url','name']        




class UserSignUpSerializer(serializers.Serializer):

    
    email = serializers.EmailField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    username = serializers.CharField(
        min_length = 4,
        max_length = 20,
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    # user = UserModelSerializer(many=False)

    password = serializers.CharField(min_length=8,max_length=64)
    password_confirmation = serializers.CharField(min_length=8,max_length=64)
    activo = serializers.IntegerField()
    # first_name = serializers.CharField(min_length =2, max_length=30)
    def validate(self , data):
        
        passwd = data['password']
        passwd_conf = data['password_confirmation']

        if passwd != passwd_conf:
            raise serializers.ValidationError("Password do not match.")
        password_validation.validate_password(passwd)
        
        return data

    def create(self,data):
        # return data
        remo = data.pop('password_confirmation')
        # print(**data)
        user = User.objects.create_user(**data)
       
      
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self,data):
            username = data['email']
            password = data['password']
            user = authenticate(username="samueld.reyesm@gmail.com",password=password)
            # return data
            if not user :
                raise serializers.ValidationError(user)
            
        
            
            self.context['user'] = user
            return data

    



