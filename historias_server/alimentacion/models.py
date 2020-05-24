from django.db import models
from shortuuidfield import ShortUUIDField

class DatosAlimentacion(models.Model):
    nombre_alimento = models.CharField(blank=True, max_length=30, verbose_name="nombres")
    descripcion = models.TextField(default="")
    unidad = models.FloatField(null=True, blank=True, default=None)
    cant_sodio = models.FloatField(null=True, blank=True, default=None)
    cant_calcio = models.FloatField(null=True, blank=True, default=None)
    cant_magnesio = models.FloatField(null=True, blank=True, default=None)
    calorias = models.FloatField(null=True, blank=True, default=None)
    proteina = models.FloatField(null=True, blank=True, default=None)
    carbohidratos = models.FloatField(null=True, blank=True, default=None)
    grasas = models.FloatField(null=True, blank=True, default=None)
    lista_negra = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Alimentacion(DatosAlimentacion):
    uuid = ShortUUIDField()