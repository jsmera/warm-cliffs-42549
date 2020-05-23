from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy
from .models import HistoriaClinica
from historias_server.user.models import Paciente
from .forms import CreateHistoriaForm, UpdateHistoriaForm
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin


class CreateHistoriaView(LoginRequiredMixin, CreateView):
    template_name = "historias/historia_create.html"
    model = HistoriaClinica
    form_class = CreateHistoriaForm

    def form_valid(self, form):
        form.instance.paciente = get_object_or_404(Paciente, uuid = self.kwargs["uuid"])
        return super(CreateHistoriaView, self).form_valid(form)

    def get_success_url(self):
        return reverse("historias:lista-historias",  kwargs={'uuid': self.kwargs["uuid"]})


class UpdateHistoriaView(LoginRequiredMixin, UpdateView):
    template_name = "historias/historia_update.html"
    model = HistoriaClinica
    form_class = UpdateHistoriaForm
    
    def get_object(self, queryset=None):
        obj = get_object_or_404(HistoriaClinica, uuid=self.kwargs["uuid2"])
        return obj
    
    def get_success_url(self):
        paciente = get_object_or_404(Paciente, uuid = self.kwargs["uuid"])
        return reverse("historias:lista-historias",  kwargs={'uuid': self.kwargs["uuid"]})
    
 

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
        fecha_creacion = self.request.GET.get('fecha_creacion', "")
        query = HistoriaClinica.objects.filter(fecha_creacion__icontains=fecha_creacion, paciente__uuid = self.kwargs["uuid"])
        return query
    
    def get_object(self, queryset=None):
        obj = get_object_or_404(HistoriaClinica, paciente__uuid = self.kwargs["uuid"])
        return obj

    def get_context_data(self, **kwargs):
        base_url = self.request.GET.copy()
        if "page" in base_url:
            base_url.pop("page")
        context = super(HistoriaListView, self).get_context_data(**kwargs)
        context["paciente"] = get_object_or_404(Paciente, uuid = self.kwargs["uuid"])
        context["fecha_creacion"] = self.request.GET.get('fecha_creacion', "")
        context["base_url"] = base_url.urlencode

        return context

