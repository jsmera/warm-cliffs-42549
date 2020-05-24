from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Alimentacion

class CreateAlimentacionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateAlimentacionForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Alimentacion
        fields = [
            "nombre_alimento",
            "descripcion",
            "unidad",
            "cant_sodio",
            "cant_calcio",
            "cant_magnesio",
            "calorias",
            "proteina",
            "carbohidratos",
            "grasas",
            "lista_negra",
        ]

        labels = {
            "nombre_alimento":"nombre_alimento",
            "descripcion":"descripcion",
            "unidad":"unidad",
            "cant_sodio":"cant_sodio",
            "cant_calcio":"cant_calcio",
            "cant_magnesio":"cant_magnesio",
            "calorias":"calorias",
            "proteina":"proteina",
            "carbohidratos":"carbohidratos",
            "grasas":"grasas",
            "lista_negra":"lista_negra", 
        }
   

class UpdateAlimentacionForm(ModelForm):
    class Meta:
        model = Alimentacion
        fields = [
            "nombre_alimento",
            "descripcion",
            "unidad",
            "cant_sodio",
            "cant_calcio",
            "cant_magnesio",
            "calorias",
            "proteina",
            "carbohidratos",
            "grasas",
            "lista_negra",
        ]

        labels = {
            "nombre_alimento":"nombre_alimento",
            "descripcion":"descripcion",
            "unidad":"unidad",
            "cant_sodio":"cant_sodio",
            "cant_calcio":"cant_calcio",
            "cant_magnesio":"cant_magnesio",
            "calorias":"calorias",
            "proteina":"proteina",
            "carbohidratos":"carbohidratos",
            "grasas":"grasas",
            "lista_negra":"lista_negra", 
        }
    