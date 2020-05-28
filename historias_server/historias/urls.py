from .views import (
    CreateHistoriaView,
    HistoriaListView,
    UpdateHistoriaView,
    DeleteHistoriaView,
)
from django.conf.urls import url

urlpatterns = [
    url(
        r"^(?P<uuid>[-\w]+)/historias/lista-historias/$",
        HistoriaListView.as_view(),
        name="lista-historias",
    ),
    url(
        r"^(?P<uuid>[-\w]+)/historias/crear-historias/$",
        CreateHistoriaView.as_view(),
        name="crear-historias",
    ),
    url(
        r"^historias/(?P<uuid>[-\w]+)/(?P<uuid2>[-\w]+)/editar-historias/$",
        UpdateHistoriaView.as_view(),
        name="editar-historias",
    ),
    url(
        r"^historias/(?P<uuid>[-\w]+)/eliminar-historias/$",
        DeleteHistoriaView.as_view(),
        name="eliminar-historias",
    ),
]
