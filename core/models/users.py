from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
from core.models.total import CustomUserManager
class User(AbstractBaseUser):
    # userid = models.AutoField('id',primary_key=True)
    objects =  CustomUserManager()
    email=models.CharField("Email",max_length=50)
    password =models.CharField("Password",max_length=128)
    username=models.CharField("Username",max_length=30)
    activo=models.IntegerField("Activo")
    def __str__(self):
	    return self.id
