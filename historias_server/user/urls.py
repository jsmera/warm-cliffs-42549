from .views import CreateUsuarioView, UsuarioListView, UpdateUsuarioView, DeleteUsuarioView
from .views import CreatePacienteView, PacienteListView, UpdatePacienteView, DeletePacienteView
from django.conf.urls import url

urlpatterns = [
    url(r"^$", UsuarioListView.as_view(), name="lista"),
    url(r"^crear/$", CreateUsuarioView.as_view(), name="crear"),
    url(r"^(?P<uuid>[-\w]+)/$", UpdateUsuarioView.as_view(), name="editar"),
    url(r"^(?P<uuid>[-\w]+)/eliminar/$", DeleteUsuarioView.as_view(), name="eliminar"),

    url(r"^pacientes/lista-pacientes/$", PacienteListView.as_view(), name="lista-pacientes"),
    url(r"^pacientes/crear-pacientes/$", CreatePacienteView.as_view(), name="crear-pacientes"),
    url(r"^pacientes/(?P<uuid>[-\w]+)/editar-pacientes/$", UpdatePacienteView.as_view(), name="editar-pacientes"),
    url(r"^pacientes/(?P<uuid>[-\w]+)/eliminar-pacientes/$", DeletePacienteView.as_view(), name="eliminar-pacientes"),
]
