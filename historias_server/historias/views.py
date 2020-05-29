from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy
from django.core.mail import send_mail
from .models import (
    HistoriaClinica,
    LineaAlergia,
    LineaConsumo,
    LineaMedicamento,
    LineaReceta,
    LineaDieta,
    Pregunta,
    LineaEnfermedad,
    Enfermedad,
)
from django.views import View
from historias_server.user.models import Paciente
from .forms import (
    CreateHistoriaForm,
    UpdateHistoriaForm,
    CreateEnfermedadForm,
    UpdateEnfermedadForm,
)
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from wkhtmltopdf.views import PDFTemplateView


class CreateHistoriaView(LoginRequiredMixin, CreateView):
    template_name = "historias/historia_create.html"
    model = HistoriaClinica
    form_class = CreateHistoriaForm
    AlergiasInlineFormSet = inlineformset_factory(
        HistoriaClinica,
        LineaAlergia,
        fields=("causa", "efectos_secundarios",),
        extra=1,
    )
    ConsumoInlineFormSet = inlineformset_factory(
        HistoriaClinica, LineaConsumo, fields=("alimento", "frecuencia",), extra=1,
    )
    MedicamentoInlineFormSet = inlineformset_factory(
        HistoriaClinica,
        LineaMedicamento,
        fields=("medicamento", "posologia", "frecuencia",),
        extra=1,
    )
    RecetaInlineFormSet = inlineformset_factory(
        HistoriaClinica,
        LineaReceta,
        fields=("medicamento", "posologia", "frecuencia",),
        extra=1,
    )
    DietaInlineFormSet = inlineformset_factory(
        HistoriaClinica,
        LineaDieta,
        fields=("alimento", "cantidad", "frecuencia",),
        extra=1,
    )
    PreguntaInlineFormSet = inlineformset_factory(
        HistoriaClinica, Pregunta, fields=("pregunta", "respuesta",), extra=1,
    )
    LineaEnfermedadInlineFormSet = inlineformset_factory(
        HistoriaClinica, LineaEnfermedad, fields=("enfermedad",), extra=1,
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["alergias_form"] = self.AlergiasInlineFormSet()
        context["consumo_form"] = self.ConsumoInlineFormSet()
        context["medicamentos_form"] = self.MedicamentoInlineFormSet()
        context["receta_form"] = self.RecetaInlineFormSet()
        context["dieta_form"] = self.DietaInlineFormSet()
        context["pregunta_form"] = self.PreguntaInlineFormSet()
        context["enfermedad_form"] = self.LineaEnfermedadInlineFormSet()
        return context

    def form_valid(self, form):
        form.instance.paciente = get_object_or_404(Paciente, uuid=self.kwargs["uuid"])
        form.instance.nutricionista = self.request.user
        return super(CreateHistoriaView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        alergias_form = self.AlergiasInlineFormSet(self.request.POST)
        consumo_form = self.ConsumoInlineFormSet(self.request.POST)
        medicamentos_form = self.MedicamentoInlineFormSet(self.request.POST)
        receta_form = self.RecetaInlineFormSet(self.request.POST)
        dieta_form = self.DietaInlineFormSet(self.request.POST)
        pregunta_form = self.PreguntaInlineFormSet(self.request.POST)
        enfermedad_form = self.LineaEnfermedadInlineFormSet(self.request.POST)
        if (
            form.is_valid()
            and alergias_form.is_valid()
            and consumo_form.is_valid()
            and medicamentos_form.is_valid()
            and receta_form.is_valid()
            and dieta_form.is_valid()
            and pregunta_form.is_valid()
            and enfermedad_form.is_valid()
        ):
            prevent = self.form_valid(form)
            alergias_form.instance = form.instance
            alergias_form.save()
            consumo_form.instance = form.instance
            consumo_form.save()
            medicamentos_form.instance = form.instance
            medicamentos_form.save()
            receta_form.instance = form.instance
            receta_form.save()
            dieta_form.instance = form.instance
            dieta_form.save()
            pregunta_form.instance = form.instance
            pregunta_form.save()
            enfermedad_form.instance = form.instance
            enfermedad_form.save()
            return prevent
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse(
            "historias:lista-historias", kwargs={"uuid": self.kwargs["uuid"]}
        )


class UpdateHistoriaView(LoginRequiredMixin, UpdateView):
    template_name = "historias/historia_update.html"
    model = HistoriaClinica
    form_class = UpdateHistoriaForm
    AlergiasInlineFormSet = inlineformset_factory(
        HistoriaClinica,
        LineaAlergia,
        fields=("causa", "efectos_secundarios",),
        extra=1,
    )
    ConsumoInlineFormSet = inlineformset_factory(
        HistoriaClinica, LineaConsumo, fields=("alimento", "frecuencia",), extra=1,
    )
    MedicamentoInlineFormSet = inlineformset_factory(
        HistoriaClinica,
        LineaMedicamento,
        fields=("medicamento", "posologia", "frecuencia",),
        extra=1,
    )
    RecetaInlineFormSet = inlineformset_factory(
        HistoriaClinica,
        LineaReceta,
        fields=("medicamento", "posologia", "frecuencia",),
        extra=1,
    )
    DietaInlineFormSet = inlineformset_factory(
        HistoriaClinica,
        LineaDieta,
        fields=("alimento", "cantidad", "frecuencia",),
        extra=1,
    )
    PreguntaInlineFormSet = inlineformset_factory(
        HistoriaClinica, Pregunta, fields=("pregunta", "respuesta",), extra=1,
    )
    LineaEnfermedadInlineFormSet = inlineformset_factory(
        HistoriaClinica, LineaEnfermedad, fields=("enfermedad",), extra=1,
    )

    def get_object(self, queryset=None):
        obj = get_object_or_404(HistoriaClinica, uuid=self.kwargs["uuid2"])
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["alergias_form"] = self.AlergiasInlineFormSet(instance=self.object)
        context["consumo_form"] = self.ConsumoInlineFormSet(instance=self.object)
        context["medicamentos_form"] = self.MedicamentoInlineFormSet(
            instance=self.object
        )
        context["receta_form"] = self.RecetaInlineFormSet(instance=self.object)
        context["dieta_form"] = self.DietaInlineFormSet(instance=self.object)
        context["pregunta_form"] = self.PreguntaInlineFormSet(instance=self.object)
        context["enfermedad_form"] = self.LineaEnfermedadInlineFormSet(
            instance=self.object
        )
        return context

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        self.object = self.get_object()
        form = self.get_form()
        alergias_form = self.AlergiasInlineFormSet(
            self.request.POST, instance=self.object
        )
        consumo_form = self.ConsumoInlineFormSet(
            self.request.POST, instance=self.object
        )
        medicamentos_form = self.MedicamentoInlineFormSet(
            self.request.POST, instance=self.object
        )
        dieta_form = self.DietaInlineFormSet(self.request.POST, instance=self.object)
        receta_form = self.RecetaInlineFormSet(self.request.POST, instance=self.object)
        pregunta_form = self.PreguntaInlineFormSet(
            self.request.POST, instance=self.object
        )
        enfermedad_form = self.LineaEnfermedadInlineFormSet(
            self.request.POST, instance=self.object
        )
        if (
            form.is_valid()
            and alergias_form.is_valid()
            and consumo_form.is_valid()
            and medicamentos_form.is_valid()
            and receta_form.is_valid()
            and dieta_form.is_valid()
            and pregunta_form.is_valid()
            and enfermedad_form.is_valid()
        ):
            prevent = self.form_valid(form)
            alergias_form.instance = form.instance
            alergias_form.save()
            consumo_form.instance = form.instance
            consumo_form.save()
            medicamentos_form.instance = form.instance
            medicamentos_form.save()
            receta_form.instance = form.instance
            receta_form.save()
            dieta_form.instance = form.instance
            dieta_form.save()
            pregunta_form.instance = form.instance
            pregunta_form.save()
            enfermedad_form.instance = form.instance
            enfermedad_form.save()
            return prevent
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse(
            "historias:lista-historias", kwargs={"uuid": self.kwargs["uuid"]}
        )


class DeleteHistoriaView(LoginRequiredMixin, DeleteView):
    model = HistoriaClinica
    success_url = reverse_lazy("historias:lista-historias")

    def get_object(self, queryset=None):
        obj = get_object_or_404(HistoriaClinica, uuid=self.kwargs["uuid"])
        return obj


class HistoriaListView(LoginRequiredMixin, ListView):
    template_name = "historias/historia_list.html"
    model = HistoriaClinica
    paginate_by = 10

    def get_queryset(self):
        fecha_creacion = self.request.GET.get("fecha_creacion", "")
        query = HistoriaClinica.objects.filter(
            fecha_creacion__icontains=fecha_creacion, paciente__uuid=self.kwargs["uuid"]
        )
        return query

    def get_object(self, queryset=None):
        obj = get_object_or_404(HistoriaClinica, paciente__uuid=self.kwargs["uuid"])
        return obj

    def get_context_data(self, **kwargs):
        base_url = self.request.GET.copy()
        if "page" in base_url:
            base_url.pop("page")
        context = super(HistoriaListView, self).get_context_data(**kwargs)
        context["paciente"] = get_object_or_404(Paciente, uuid=self.kwargs["uuid"])
        context["fecha_creacion"] = self.request.GET.get("fecha_creacion", "")
        context["base_url"] = base_url.urlencode

        return context


class SendReceipt(LoginRequiredMixin, View):
    def get(self, request, uuid, *args, **kwargs):
        historia = get_object_or_404(HistoriaClinica, uuid=uuid)
        historia.enviar_recetas()
        return redirect(
            reverse(
                "historias:lista-historias", kwargs={"uuid": historia.paciente.uuid}
            )
        )


class HistoriaPDFReportView(LoginRequiredMixin, PDFTemplateView):
    template_name = "historias/pdf_report.html"
    filename = None
    cmd_options = {
        "margin-top": 20,
        "margin-left": 20,
        "margin-right": 20,
        "margin-bottom": 20,
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["historia"] = get_object_or_404(HistoriaClinica, uuid=kwargs["uuid"])
        return context


class CreateEnfermedadView(LoginRequiredMixin, CreateView):
    template_name = "historias/enfermedad_create.html"
    model = Enfermedad
    form_class = CreateEnfermedadForm

    def get_success_url(self):
        return reverse("historias:lista-enfermedad")


class UpdateEnfermedadView(LoginRequiredMixin, UpdateView):
    template_name = "historias/enfermedad_update.html"
    model = Enfermedad
    form_class = UpdateEnfermedadForm

    def get_success_url(self):
        return reverse("historias:lista-enfermedad")

    def get_object(self, queryset=None):
        obj = get_object_or_404(Enfermedad, uuid=self.kwargs["uuid"])
        return obj


class DeleteEnfermedadView(LoginRequiredMixin, DeleteView):
    model = Enfermedad
    success_url = reverse_lazy("historias:lista-enfermedad")

    def get_object(self, queryset=None):
        obj = get_object_or_404(Enfermedad, uuid=self.kwargs["uuid"])
        return obj


class EnfermedadListView(LoginRequiredMixin, ListView):
    model = Enfermedad
    template_name = "historias/enfermedad_list.html"
    paginate_by = 10

    def get_queryset(self):
        nombre_enfermedad = self.request.GET.get("nombre_enfermedad", "")

        query = Enfermedad.objects.filter((Q(nombre__icontains=nombre_enfermedad)))
        return query

    def get_context_data(self, **kwargs):
        base_url = self.request.GET.copy()
        if "page" in base_url:
            base_url.pop("page")
        context = super(EnfermedadListView, self).get_context_data(**kwargs)

        return context
