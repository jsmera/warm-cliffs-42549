from django.contrib import admin
from .models import Usuario
from .forms import UsuarioForm

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    pass


admin.site.register(Usuario, UsuarioAdmin)
