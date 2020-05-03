from django.contrib import admin
from .models import Usuario
from .forms import CreateUsuarioForm

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    pass


admin.site.register(Usuario, UsuarioAdmin)
