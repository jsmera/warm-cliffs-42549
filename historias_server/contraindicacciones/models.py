from django.db import models
from django.contrib.auth.models import AbstractUser
from shortuuidfield import ShortUUIDField


class Contraindicacciones(models.Model):
    medicamento = models.ForeignKey(
        'medicacion.Medicacion',
        models.SET_NULL,
        blank=True,
        null=True,
    )
    alimento = models.ForeignKey(
        'alimentacion.Alimentacion',
        models.SET_NULL,
        blank=True,
        null=True,
    )
    uuid = ShortUUIDField()