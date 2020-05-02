from .views import CreateUsuarioView, UsuarioListView
from django.conf.urls import url

urlpatterns = [
    url(r"^$", UsuarioListView.as_view(), name="lista"),
    url(r"^crear/$", CreateUsuarioView.as_view(), name="crear")
]
