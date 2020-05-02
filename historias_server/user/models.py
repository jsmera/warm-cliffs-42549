from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.


class Usuario(AbstractUser):
    TIPO_DOCUMENTO = [("CC", "Cedula"), ("TI", "Tarjeta de identidad")]
    GENERO = [("F", "Femenino"), ("M", "Masculino")]
    ESTADO = [("SO", "Soltero"), ("CA", "Casado"), ("DI", "Divorciado")]
    ROLES = [("admin", "Administrador"), ("nutri", "Nutricionista")]
    fecha_nacimiento = models.DateField(default=timezone.now)
    tipo_documento = models.CharField(
        max_length=2, choices=TIPO_DOCUMENTO, default="CC",
    )
    genero = models.CharField(max_length=2, choices=GENERO, default="M",)
    num_documento = models.CharField(default="", max_length=20)
    estado_civil = models.CharField(max_length=2, choices=ESTADO, default="SO",)
    telefono = models.CharField(default="", max_length=50)
    direccion = models.CharField(default="", max_length=100)
    rol = models.CharField(max_length=5, choices=ROLES, default="nutri",)
