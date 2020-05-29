from django.db import models
from django.contrib.auth.models import AbstractUser
from shortuuidfield import ShortUUIDField
from django.utils import timezone


class Perfil(models.Model):
    TIPO_DOCUMENTO = [("CC", "Cedula"), ("TI", "Tarjeta de identidad")]
    GENERO = [("F", "Femenino"), ("M", "Masculino")]
    ESTADO = [("SO", "Soltero"), ("CA", "Casado"), ("DI", "Divorciado")]
    first_name = models.CharField(max_length=30, verbose_name="nombres", blank=True)
    last_name = models.CharField(max_length=150, verbose_name="apellidos", blank=True)
    email = models.EmailField(
        blank=False, max_length=254, verbose_name="correo electrónico"
    )
    fecha_nacimiento = models.DateField(default=timezone.now)
    tipo_documento = models.CharField(
        max_length=2, choices=TIPO_DOCUMENTO, default="CC", blank=False
    )
    genero = models.CharField(max_length=2, choices=GENERO, default="M", blank=False)
    num_documento = models.CharField(max_length=20, blank=False)
    estado_civil = models.CharField(
        max_length=2, choices=ESTADO, default="SO", blank=False
    )
    telefono = models.CharField(max_length=50, blank=False)
    direccion = models.CharField(max_length=100, blank=False)

    class Meta:
        abstract = True

    @property
    def nombre_perfil(self):
        name = ""
        if self.first_name:
            name += self.first_name
        if self.last_name:
            name += " " + self.last_name
        return name


class AbstractCustomUser(AbstractUser):
    first_name = None
    last_name = None
    email = None

    class Meta:
        abstract = True


class Usuario(Perfil, AbstractCustomUser):
    ROLES = [("admin", "Administrador"), ("nutri", "Nutricionista")]
    uuid = ShortUUIDField()
    rol = models.CharField(max_length=5, choices=ROLES, default="nutri")


class Paciente(Perfil):
    uuid = ShortUUIDField()
    nutricionista = models.ForeignKey(
        "user.Usuario", models.SET_NULL, blank=True, null=True,
    )
