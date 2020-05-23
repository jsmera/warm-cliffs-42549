from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import HistoriaClinica

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
            "duracion_ejercicio":"Duracion del ejercicio",
            "frecuencia_ejercicio":"Frecuencia del ejercicio",
            "inicio_ejercicio":"Inicio del ejercicio",
            "nivel_apetito":"Nivel del apetito",
            "hora_mayor_apetito":"Hora de mayor apetito",
            "diagnostico":"Diagnostico",
            "cant_comidas":"Cantidad de comidas al dia",
            "peso_actual":"Peso actual",
            "peso_habitual":"Peso habitual",
            "estatura":"Estatura",
            "pliegueCutaneoTri":"Pliegue Cutaneo tricipital",
            "pliegueCutaneoBi":"Pliegue Cutaneo bicipital",
            "pliegueCutaneoSub":"Pliegue Cutaneo subescapular",
            "pliegueCutaneoSupra":"Pliegue Cutaneo suprailiaco",
            "circ_brazo":"Circunferencia de brazo",
            "circ_cintura":"Circunferencia de cintura",
            "circ_cadera":"Circircunferencia de cadera",
            "circ_abdominal":"Circunferencia abdominal",
            "peso_teorico":"Peso teorico",
            "porcent_peso_teorico":"Porcentaje peso teorico",
            "porcent_peso_habitual":"Porcentaje peso habitual",
            "indice_masa_corporal":"Indice de masa corporal",
            "porcent_grasa_corporal":"Porcentaje de grasa corporal",
            "grasa_corporal_tot":"Grasa corporal total",
            "masa_libre_grasa":"Masa libre de grasa",
            "masa_muscular_total":"Masa muscular total",
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
            "duracion_ejercicio":"Duracion del ejercicio",
            "frecuencia_ejercicio":"Frecuencia del ejercicio",
            "inicio_ejercicio":"Inicio del ejercicio",
            "nivel_apetito":"Nivel del apetito",
            "hora_mayor_apetito":"Hora de mayor apetito",
            "diagnostico":"Diagnostico",
            "cant_comidas":"Cantidad de comidas al dia",
            "peso_actual":"Peso actual",
            "peso_habitual":"Peso habitual",
            "estatura":"Estatura",
            "pliegueCutaneoTri":"Pliegue Cutaneo tricipital",
            "pliegueCutaneoBi":"Pliegue Cutaneo bicipital",
            "pliegueCutaneoSub":"Pliegue Cutaneo subescapular",
            "pliegueCutaneoSupra":"Pliegue Cutaneo suprailiaco",
            "circ_brazo":"Circunferencia de brazo",
            "circ_cintura":"Circunferencia de cintura",
            "circ_cadera":"Circircunferencia de cadera",
            "circ_abdominal":"Circunferencia abdominal",
            "peso_teorico":"Peso teorico",
            "porcent_peso_teorico":"Porcentaje peso teorico",
            "porcent_peso_habitual":"Porcentaje peso habitual",
            "indice_masa_corporal":"Indice de masa corporal",
            "porcent_grasa_corporal":"Porcentaje de grasa corporal",
            "grasa_corporal_tot":"Grasa corporal total",
            "masa_libre_grasa":"Masa libre de grasa",
            "masa_muscular_total":"Masa muscular total",
        }
    