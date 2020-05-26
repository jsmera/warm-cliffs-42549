from django.db import models
from shortuuidfield import ShortUUIDField

class DatosMedicacion(models.Model):
    nombre_medicamento = models.CharField(blank=True, max_length=30, verbose_name="nombres")
    descripcion = models.TextField(default="", blank=True)
    unidad = models.FloatField(null=True, blank=True, default=None)
    cant_sodio = models.FloatField(null=True, blank=True, default=None)
    cant_calcio = models.FloatField(null=True, blank=True, default=None)
    cant_magnesio = models.FloatField(null=True, blank=True, default=None)

    class Meta:
        abstract = True


class Medicacion(DatosMedicacion):
    uuid = ShortUUIDField()