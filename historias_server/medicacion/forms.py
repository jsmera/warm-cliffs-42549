from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Medicacion

class CreateMedicacionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateMedicacionForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Medicacion
        fields = [
            "nombre_medicamento",
            "descripcion",
            "unidad",
            "cant_sodio",
            "cant_calcio",
            "cant_magnesio",
        ]

        labels = {
            "nombre_medicamento":"nombre del medicamento",
            "descripcion":"descripcion",
            "unidad":"unidad",
            "cant_sodio":"cantidad de sodio",
            "cant_calcio":"cantidad de calcio",
            "cant_magnesio":"cantidad de magnesio",
        }
   

class UpdateMedicacionForm(ModelForm):
    class Meta:
        model = Medicacion
        fields = [
            "nombre_medicamento",
            "descripcion",
            "unidad",
            "cant_sodio",
            "cant_calcio",
            "cant_magnesio",
        
        ]

        labels = {
            "nombre_medicamento":"nombre del medicamento",
            "descripcion":"descripcion",
            "unidad":"unidad",
            "cant_sodio":"cantidad de sodio",
            "cant_calcio":"cantidad de calcio",
            "cant_magnesio":"cantidad de magnesio",
        }
    