from django.db import models
from django.contrib.auth.models import AbstractUser
from shortuuidfield import ShortUUIDField
from django.utils import timezone
import datetime


class DatosHistoria(models.Model):
    FRECUENCIA = [
        ("0D", "0 Dias"),
        ("1D", "1 Dia"),
        ("2D", "2 Dias"),
        ("3D", "3 Dias"),
        ("4D", "4 Dias"),
        ("5D", "5 Dias"),
        ("6D", "6 Dias"),
        ("7D", "7 Dias"),
    ]
    APETITO = [("BA", "Bajo"), ("ME", "Medio"), ("AL", "Alto")]
    HORA = [
        ("0h", "0 AM"),
        ("1h", "1 AM"),
        ("2h", "2 AM"),
        ("3h", "3 AM"),
        ("4h", "4 AM"),
        ("5h", "5 AM"),
        ("6h", "6 AM"),
        ("7h", "7 AM"),
        ("8h", "8 AM"),
        ("9h", "9 AM"),
        ("10h", "10 AM"),
        ("11h", "11 AM"),
        ("12h", "12 PM"),
        ("13h", "1 PM"),
        ("14h", "2 PM"),
        ("15h", "3 PM"),
        ("16h", "4 PM"),
        ("17h", "5 PM"),
        ("18h", "6 PM"),
        ("19h", "7 PM"),
        ("20h", "8 PM"),
        ("21h", "9 PM"),
        ("22h", "10 PM"),
        ("23h", "11 PM"),
    ]

    fecha_creacion = models.DateField(default=datetime.datetime.now)
    fecha_actualizacion = models.DateField(auto_now=True)
    # poner esto en char o float
    duracion_ejercicio = models.FloatField(null=True, blank=True, default=None)
    frecuencia_ejercicio = models.CharField(
        max_length=2, choices=FRECUENCIA, default="0D",
    )
    inicio_ejercicio = models.DateField(default=datetime.datetime.now)
    nivel_apetito = models.CharField(max_length=2, choices=APETITO, default="AL",)
    hora_mayor_apetito = models.CharField(max_length=4, choices=HORA, default="0h",)
    diagnostico = models.TextField(default="", blank=True)
    cant_comidas = models.IntegerField(null=True, blank=True, default=None)
    peso_actual = models.FloatField(null=True, blank=True, default=None)
    peso_habitual = models.FloatField(null=True, blank=True, default=None)
    estatura = models.IntegerField(null=True, blank=True, default=None)
    pliegueCutaneoTri = models.FloatField(null=True, blank=True, default=None)
    pliegueCutaneoBi = models.FloatField(null=True, blank=True, default=None)
    pliegueCutaneoSub = models.FloatField(null=True, blank=True, default=None)
    pliegueCutaneoSupra = models.FloatField(null=True, blank=True, default=None)
    circ_brazo = models.FloatField(null=True, blank=True, default=None)
    circ_cintura = models.FloatField(null=True, blank=True, default=None)
    circ_cadera = models.FloatField(null=True, blank=True, default=None)
    circ_abdominal = models.FloatField(null=True, blank=True, default=None)
    peso_teorico = models.FloatField(null=True, blank=True, default=None)
    porcent_peso_teorico = models.FloatField(null=True, blank=True, default=None)
    porcent_peso_habitual = models.FloatField(null=True, blank=True, default=None)
    indice_masa_corporal = models.FloatField(null=True, blank=True, default=None)
    porcent_grasa_corporal = models.FloatField(null=True, blank=True, default=None)
    grasa_corporal_tot = models.FloatField(null=True, blank=True, default=None)
    masa_libre_grasa = models.FloatField(null=True, blank=True, default=None)
    masa_muscular_total = models.FloatField(null=True, blank=True, default=None)

    class Meta:
        abstract = True


class HistoriaClinica(DatosHistoria):
    nutricionista = models.ForeignKey(
        "user.Usuario", models.SET_NULL, blank=True, null=True,
    )
    paciente = models.ForeignKey(
        "user.Paciente", models.SET_NULL, blank=True, null=True,
    )
    uuid = ShortUUIDField()


class LineaAlergia(models.Model):
    hisotoria_clinica = models.ForeignKey(
        "historias.HistoriaClinica", models.SET_NULL, blank=True, null=True,
    )
    causa = models.ForeignKey(
        "alimentacion.Alimentacion", models.SET_NULL, blank=True, null=True,
    )
    efectos_secundarios = models.CharField(max_length=200)


class LineaConsumo(models.Model):
    FRECUENCIA = [
        ("0", "Muy baja"),
        ("1", "Baja"),
        ("2", "Media"),
        ("3", "Alta"),
        ("4", "Muy alta"),
    ]
    hisotoria_clinica = models.ForeignKey(
        "historias.HistoriaClinica", models.SET_NULL, blank=True, null=True,
    )
    alimento = models.ForeignKey(
        "alimentacion.Alimentacion", models.SET_NULL, blank=True, null=True,
    )
    frecuencia = models.CharField(max_length=2, choices=FRECUENCIA, default="0",)


class LineaMedicamento(models.Model):
    FRECUENCIA = [
        ("2", "Cada 2 horas"),
        ("3", "Cada 3 horas"),
        ("4", "Cada 4 horas"),
        ("5", "Cada 5 horas"),
        ("6", "Cada 6 horas"),
        ("12", "Cada 12 horas"),
    ]
    hisotoria_clinica = models.ForeignKey(
        "historias.HistoriaClinica", models.SET_NULL, blank=True, null=True,
    )
    medicamento = models.ForeignKey(
        "medicacion.Medicacion", models.SET_NULL, blank=True, null=True,
    )
    posologia = models.FloatField(null=True, blank=True, default=1.0)
    frecuencia = models.CharField(max_length=2, choices=FRECUENCIA, default="2",)


class LineaReceta(models.Model):
    FRECUENCIA = [
        ("2", "Cada 2 horas"),
        ("3", "Cada 3 horas"),
        ("4", "Cada 4 horas"),
        ("5", "Cada 5 horas"),
        ("6", "Cada 6 horas"),
        ("12", "Cada 12 horas"),
    ]
    hisotoria_clinica = models.ForeignKey(
        "historias.HistoriaClinica", models.SET_NULL, blank=True, null=True,
    )
    medicamento = models.ForeignKey(
        "medicacion.Medicacion", models.SET_NULL, blank=True, null=True,
    )
    posologia = models.FloatField(null=True, blank=True, default=1.0)
    frecuencia = models.CharField(max_length=2, choices=FRECUENCIA, default="2",)


class LineaDieta(models.Model):
    FRECUENCIA = [
        ("2", "Cada 2 horas"),
        ("3", "Cada 3 horas"),
        ("4", "Cada 4 horas"),
        ("5", "Cada 5 horas"),
        ("6", "Cada 6 horas"),
        ("12", "Cada 12 horas"),
    ]
    hisotoria_clinica = models.ForeignKey(
        "historias.HistoriaClinica", models.SET_NULL, blank=True, null=True,
    )
    cantidad = models.FloatField(null=True, blank=True, default=1.0)
    alimento = models.ForeignKey(
        "alimentacion.Alimentacion", models.SET_NULL, blank=True, null=True,
    )
    frecuencia = models.CharField(max_length=2, choices=FRECUENCIA, default="2",)


class Pregunta(models.Model):
    hisotoria_clinica = models.ForeignKey(
        "historias.HistoriaClinica", models.SET_NULL, blank=True, null=True,
    )
    pregunta = models.CharField(max_length=100)
    respuesta = models.CharField(max_length=500)
