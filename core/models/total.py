from django.db import models
from django.forms import IntegerField
from django.contrib.auth.models import AbstractBaseUser, UserManager

class Total(models.Model):
    total= models.IntegerField('total mensual',max_length=255)
    ahorro= models.IntegerField('ahorro mensual',max_length=255)
    gastos = models.IntegerField('gasto mensual',max_length=255)
    ahorro_anual = models.IntegerField('ahorro anual',max_length=255)


    
class CustomUserManager(UserManager):
    def create_user(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, **extra_fields)