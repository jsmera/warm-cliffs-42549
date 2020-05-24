from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy
from .models import Medicacion
from .forms import CreateMedicacionForm, UpdateMedicacionForm
from django.db.models import Q

class CreateMedicacionView(LoginRequiredMixin, CreateView):
    template_name = "medicacion/medicacion_create.html"
    model = Medicacion
    form_class = CreateMedicacionForm

    def get_success_url(self):
        return reverse("medicacion:lista-medicacion")

class UpdateMedicacionView(LoginRequiredMixin, UpdateView):
    template_name = "medicacion/medicacion_update.html"
    model = Medicacion
    form_class = UpdateMedicacionForm

    def get_success_url(self):
        return reverse("medicacion:lista-medicacion")
    
    def get_object(self, queryset=None):
        obj = get_object_or_404(Medicacion, uuid=self.kwargs["uuid"])
        return obj

class DeleteMedicacionView(LoginRequiredMixin, DeleteView):
    model = Medicacion
    success_url = reverse_lazy("medicacion:lista-medicacion")

    def get_object(self, queryset=None):
        obj = get_object_or_404(Medicacion, uuid=self.kwargs["uuid"])
        return obj


class MedicacionListView(LoginRequiredMixin, ListView):
    model = Medicacion
    paginate_by = 10
    def get_queryset(self):
        nombre_medicamento = self.request.GET.get('nombre_medicamento', "")

        query = Medicacion.objects.filter((Q(nombre_medicamento__icontains=nombre_medicamento)))
        return query
        
    def get_context_data(self, **kwargs):
        base_url = self.request.GET.copy()
        if "page" in base_url:
            base_url.pop("page")
        context = super(MedicacionListView, self).get_context_data(**kwargs)

        return context

