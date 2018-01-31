from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Usuario(AbstractUser):
    nombre = models.CharField(verbose_name='Usuario', blank=True, max_length=255)
    #wish_list = MListField(default=[], null=True, blank=True, verbose_name='List de productos deseados')
