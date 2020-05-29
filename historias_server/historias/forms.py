from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import HistoriaClinica, Enfermedad


class CreateHistoriaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateHistoriaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = HistoriaClinica
        fields = [
            "duracion_ejercicio",
            "frecuencia_ejercicio",
            "inicio_ejercicio",
            "nivel_apetito",
            "hora_mayor_apetito",
            "diagnostico",
            "cant_comidas",
            "peso_actual",
            "peso_habitual",
            "estatura",
            "pliegueCutaneoTri",
            "pliegueCutaneoBi",
            "pliegueCutaneoSub",
            "pliegueCutaneoSupra",
            "circ_brazo",
            "circ_cintura",
            "circ_cadera",
            "circ_abdominal",
            "peso_teorico",
            "porcent_peso_teorico",
            "porcent_peso_habitual",
            "indice_masa_corporal",
            "porcent_grasa_corporal",
            "grasa_corporal_tot",
            "masa_libre_grasa",
            "masa_muscular_total",
        ]

        labels = {
            "duracion_ejercicio": "Duracion del ejercicio (en minutos)",
            "frecuencia_ejercicio": "Frecuencia del ejercicio",
            "inicio_ejercicio": "Fecha de inicio del ejercicio",
            "nivel_apetito": "Nivel del apetito",
            "hora_mayor_apetito": "Hora de mayor apetito",
            "diagnostico": "Diagnostico",
            "cant_comidas": "Cantidad de comidas al dia",
            "peso_actual": "Peso actual (en kg)",
            "peso_habitual": "Peso habitual (en kg)",
            "estatura": "Estatura (en cm)",
            "pliegueCutaneoTri": "Pliegue Cutaneo tricipital (en cm)",
            "pliegueCutaneoBi": "Pliegue Cutaneo bicipital (en cm)",
            "pliegueCutaneoSub": "Pliegue Cutaneo subescapular (en cm)",
            "pliegueCutaneoSupra": "Pliegue Cutaneo suprailiaco (en cm)",
            "circ_brazo": "Circunferencia de brazo (en cm)",
            "circ_cintura": "Circunferencia de cintura (en cm)",
            "circ_cadera": "Circircunferencia de cadera (en cm)",
            "circ_abdominal": "Circunferencia abdominal (en cm)",
            "peso_teorico": "Peso teorico (en kg)",
            "porcent_peso_teorico": "Porcentaje peso teorico",
            "porcent_peso_habitual": "Porcentaje peso habitual",
            "indice_masa_corporal": "Indice de masa corporal",
            "porcent_grasa_corporal": "Porcentaje de grasa corporal",
            "grasa_corporal_tot": "Grasa corporal total",
            "masa_libre_grasa": "Masa libre de grasa",
            "masa_muscular_total": "Masa muscular total",
        }


class UpdateHistoriaForm(ModelForm):
    class Meta:
        model = HistoriaClinica
        fields = [
            "duracion_ejercicio",
            "frecuencia_ejercicio",
            "inicio_ejercicio",
            "nivel_apetito",
            "hora_mayor_apetito",
            "diagnostico",
            "cant_comidas",
            "peso_actual",
            "peso_habitual",
            "estatura",
            "pliegueCutaneoTri",
            "pliegueCutaneoBi",
            "pliegueCutaneoSub",
            "pliegueCutaneoSupra",
            "circ_brazo",
            "circ_cintura",
            "circ_cadera",
            "circ_abdominal",
            "peso_teorico",
            "porcent_peso_teorico",
            "porcent_peso_habitual",
            "indice_masa_corporal",
            "porcent_grasa_corporal",
            "grasa_corporal_tot",
            "masa_libre_grasa",
            "masa_muscular_total",
        ]

        labels = {
            "duracion_ejercicio": "Duracion del ejercicio (en minutos)",
            "frecuencia_ejercicio": "Frecuencia del ejercicio",
            "inicio_ejercicio": "Fecha de inicio del ejercicio",
            "nivel_apetito": "Nivel del apetito",
            "hora_mayor_apetito": "Hora de mayor apetito",
            "diagnostico": "Diagnostico",
            "cant_comidas": "Cantidad de comidas al dia",
            "peso_actual": "Peso actual (en kg)",
            "peso_habitual": "Peso habitual (en kg)",
            "estatura": "Estatura (en cm)",
            "pliegueCutaneoTri": "Pliegue Cutaneo tricipital (en cm)",
            "pliegueCutaneoBi": "Pliegue Cutaneo bicipital (en cm)",
            "pliegueCutaneoSub": "Pliegue Cutaneo subescapular (en cm)",
            "pliegueCutaneoSupra": "Pliegue Cutaneo suprailiaco (en cm)",
            "circ_brazo": "Circunferencia de brazo (en cm)",
            "circ_cintura": "Circunferencia de cintura (en cm)",
            "circ_cadera": "Circircunferencia de cadera (en cm)",
            "circ_abdominal": "Circunferencia abdominal (en cm)",
            "peso_teorico": "Peso teorico (en kg)",
            "porcent_peso_teorico": "Porcentaje peso teorico",
            "porcent_peso_habitual": "Porcentaje peso habitual",
            "indice_masa_corporal": "Indice de masa corporal",
            "porcent_grasa_corporal": "Porcentaje de grasa corporal",
            "grasa_corporal_tot": "Grasa corporal total",
            "masa_libre_grasa": "Masa libre de grasa",
            "masa_muscular_total": "Masa muscular total",
        }


class CreateEnfermedadForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateEnfermedadForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Enfermedad
        fields = [
            "nombre",
        ]

        labels = {
            "nombre": "Nombre de la enfermedad",
        }


class UpdateEnfermedadForm(ModelForm):
    class Meta:
        model = Enfermedad
        fields = [
            "nombre",
        ]

        labels = {
            "nombre": "Nombre de la enfermedad",
        }
