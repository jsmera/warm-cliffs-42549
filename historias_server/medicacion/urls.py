from .views import (
    CreateMedicacionView,
    MedicacionListView,
    UpdateMedicacionView,
    DeleteMedicacionView,
)
from django.conf.urls import url

urlpatterns = [
    url(
        r"^medicacion/lista-medicacion/$",
        MedicacionListView.as_view(),
        name="lista-medicacion",
    ),
    url(
        r"^medicacion/crear-medicacion/$",
        CreateMedicacionView.as_view(),
        name="crear-medicacion",
    ),
    url(
        r"^medicacion/(?P<uuid>[-\w]+)/editar-medicacion/$",
        UpdateMedicacionView.as_view(),
        name="editar-medicacion",
    ),
    url(
        r"^medicacion/(?P<uuid>[-\w]+)/eliminar-medicacion/$",
        DeleteMedicacionView.as_view(),
        name="eliminar-medicacion",
    ),
]
