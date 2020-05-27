from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Usuario
from .models import Paciente

class CreateUsuarioForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CreateUsuarioForm, self).__init__(*args, **kwargs)

        for fieldname in ["username", "password1", "password2"]:
            self.fields[fieldname].help_text = None

    class Meta:
        model = Usuario
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
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
            "genero",
        ]
        widgets = {"is_superuser": forms.HiddenInput(), "is_staff": forms.HiddenInput()}
        labels = {
            "username": "Nombre de usuario",
            "email": "Correo electrónico",
            "num_documento": "Número de documento",
            "telefono": "Teléfono",
            "direccion": "Dirección",
            "password1": "Contraseña",
            "password2": "Conformación",
            "first_name": "Nombres",
            "last_name": "Apellidos",
            "fecha_nacimiento": "Fecha de nacimiento",
            "genero":"Genero",
        }
        help_texts = {
            "username": "",
        }

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

class UpdateUsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "fecha_nacimiento",
            "tipo_documento",
            "num_documento",
            "estado_civil",
            "telefono",
            "direccion",
            "rol",
            "genero",
            "is_superuser",
            "is_staff",
        ]
        widgets = {"is_superuser": forms.HiddenInput(), "is_staff": forms.HiddenInput()}
        labels = {
            "username": "Nombre de usuario",
            "email": "Correo electrónico",
            "num_documento": "Número de documento",
            "telefono": "Teléfono",
            "direccion": "Dirección",
            "first_name": "Nombres",
            "last_name": "Apellidos",
            "fecha_nacimiento": "Fecha de nacimiento",
            "genero" : "genero",
        }
        help_texts = {
            "username": "",
        }

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


#-----------------------------------------------


class CreatePacienteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreatePacienteForm, self).__init__(*args, **kwargs)


    class Meta:
        model = Paciente
        fields = [
            "email",
            "first_name",
            "last_name",
            "fecha_nacimiento",
            "tipo_documento",
            "num_documento",
            "estado_civil",
            "telefono",
            "direccion",
            "genero"
        ]
        #widgets = {"is_superuser": forms.HiddenInput(), "is_staff": forms.HiddenInput()}
        labels = {
            "email": "Correo electrónico",
            "num_documento": "Número de documento",
            "telefono": "Teléfono",
            "direccion": "Dirección",
            "first_name": "Nombres",
            "last_name": "Apellidos",
            "fecha_nacimiento": "Fecha de nacimiento",
            "genero":"Genero"
        }


class UpdatePacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = [
            "email",
            "first_name",
            "last_name",
            "fecha_nacimiento",
            "tipo_documento",
            "num_documento",
            "estado_civil",
            "telefono",
            "direccion",
            "genero"
        ]
        labels = {
            "email": "Correo electrónico",
            "num_documento": "Número de documento",
            "telefono": "Teléfono",
            "direccion": "Dirección",
            "first_name": "Nombres",
            "last_name": "Apellidos",
            "fecha_nacimiento": "Fecha de nacimiento",
            "genero":"Genero"
        }
