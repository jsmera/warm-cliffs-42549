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
            "nombre_medicamento":"nombre medicamento",
            "descripcion":"descripcion",
            "unidad":"unidad",
            "cant_sodio":"cant_sodio",
            "cant_calcio":"cant_calcio",
            "cant_magnesio":"cant_magnesio",
        
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
            "nombre_medicamento":"nombre medicamento",
            "descripcion":"descripcion",
            "unidad":"unidad",
            "cant_sodio":"cant_sodio",
            "cant_calcio":"cant_calcio",
            "cant_magnesio":"cant_magnesio",
            
        }
    