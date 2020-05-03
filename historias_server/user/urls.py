from .views import CreateUsuarioView, UsuarioListView, UpdateUsuarioView, DeleteUsuarioView
from django.conf.urls import url

urlpatterns = [
    url(r"^$", UsuarioListView.as_view(), name="lista"),
    url(r"^crear/$", CreateUsuarioView.as_view(), name="crear"),
    url(r"^(?P<uuid>[-\w]+)/$", UpdateUsuarioView.as_view(), name="editar"),
    url(r"^(?P<uuid>[-\w]+)/eliminar/$", DeleteUsuarioView.as_view(), name="eliminar"),
]
