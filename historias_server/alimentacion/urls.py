from .views import CreateAlimentacionView, AlimentacionListView, UpdateAlimentacionView, DeleteAlimentacionView
from django.conf.urls import url

urlpatterns = [
    url(r"^alimentacion/lista-alimentacion/$", AlimentacionListView.as_view(), name="lista-alimentacion"),
    url(r"^alimentacion/crear-alimentacion/$", CreateAlimentacionView.as_view(), name="crear-alimentacion"),
    url(r"^alimentacion/(?P<uuid>[-\w]+)/editar-alimentacion/$", UpdateAlimentacionView.as_view(), name="editar-alimentacion"),
    url(r"^alimentacion/(?P<uuid>[-\w]+)/eliminar-alimentacion/$", DeleteAlimentacionView.as_view(), name="eliminar-alimentacion"),
]
