from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Usuario


class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "fecha_nacimiento",
            "tipo_documento",
            "num_documento",
            "estado_civil",
            "telefono",
            "direccion",
            "rol",
            "is_superuser",
            "is_staff",
        ]
        widgets = {"is_superuser": forms.HiddenInput(), "is_staff": forms.HiddenInput()}

    def clean_is_superuser(self):
        rol = self.cleaned_data["rol"]
        if rol == "admin":
            return True
        return False

    def clean_is_staff(self):
        rol = self.cleaned_data["rol"]
        if rol == "admin":
            return True
        return False
