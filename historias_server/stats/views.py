from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render
from historias_server.historias.models import (
    HistoriaClinica,
    LineaEnfermedad,
    LineaConsumo,
)
from django.db.models import Count
from historias_server.user.models import Usuario, Paciente


class DashboardView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        pesos = HistoriaClinica.objects.values_list("peso_actual", flat=True)
        pesos = list(filter(None, pesos))
        enfermedades = (
            LineaEnfermedad.objects.values("enfermedad__nombre")
            .annotate(cantidad=Count("enfermedad"))
            .order_by("-cantidad")[:4]
        )
        alimentos = (
            LineaConsumo.objects.values("alimento__nombre_alimento")
            .annotate(cantidad=Count("alimento"))
            .order_by("-cantidad")[:4]
        )
        nombres_enfermedades = []
        numero_enfermedades = []
        colores_enfermedades = [
            "#4acccd",
            "#fcc468",
            "#ef8157",
            "#9b59b6",
        ]
        colores_alimentos = [
            "#4acccd",
            "#fcc468",
            "#ef8157",
            "#9b59b6",
        ]
        nombres_alimentos = []
        numero_alimentos = []
        for top in alimentos:
            if top["alimento__nombre_alimento"]:
                nombres_alimentos.append(top["alimento__nombre_alimento"])
                numero_alimentos.append(top["cantidad"])
        for top in enfermedades:
            if top["enfermedad__nombre"]:
                nombres_enfermedades.append(top["enfermedad__nombre"])
                numero_enfermedades.append(top["cantidad"])
        context = {
            "n_historias": HistoriaClinica.objects.count(),
            "n_pacientes": Paciente.objects.count(),
            "n_usuarios": Usuario.objects.exclude(rol="admin").count(),
            "nombres_enfermedades": nombres_enfermedades,
            "nombres_alimentos": nombres_alimentos,
            "numero_alimentos": numero_alimentos,
            "numero_enfermedades": numero_enfermedades,
            "colores_enfermedades": colores_enfermedades[: len(numero_enfermedades)],
            "colores_alimentos": colores_alimentos[: len(numero_alimentos)],
            "pesos": pesos,
        }
        return render(request, "stats/dashboard.html", context)
