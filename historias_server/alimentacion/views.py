from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy
from .models import Alimentacion
from .forms import CreateAlimentacionForm, UpdateAlimentacionForm
from django.db.models import Q

class CreateAlimentacionView(LoginRequiredMixin, CreateView):
    template_name = "alimentacion/alimentacion_create.html"
    model = Alimentacion
    form_class = CreateAlimentacionForm

    def get_success_url(self):
        return reverse("alimentacion:lista-alimentacion")

class UpdateAlimentacionView(LoginRequiredMixin, UpdateView):
    template_name = "alimentacion/alimentacion_update.html"
    model = Alimentacion
    form_class = UpdateAlimentacionForm

    def get_success_url(self):
        return reverse("alimentacion:lista-alimentacion")
    
    def get_object(self, queryset=None):
        obj = get_object_or_404(Alimentacion, uuid=self.kwargs["uuid"])
        return obj

class DeleteAlimentacionView(LoginRequiredMixin, DeleteView):
    model = Alimentacion
    success_url = reverse_lazy("alimentacion:lista-alimentacion")

    def get_object(self, queryset=None):
        obj = get_object_or_404(Alimentacion, uuid=self.kwargs["uuid"])
        return obj


class AlimentacionListView(LoginRequiredMixin, ListView):
    model = Alimentacion
    paginate_by = 10
    def get_queryset(self):
        nombre_alimento = self.request.GET.get('nombre_alimento', "")

        query = Alimentacion.objects.filter((Q(nombre_alimento__icontains=nombre_alimento)))
        return query
        
    def get_context_data(self, **kwargs):
        base_url = self.request.GET.copy()
        if "page" in base_url:
            base_url.pop("page")
        context = super(AlimentacionListView, self).get_context_data(**kwargs)

        return context

