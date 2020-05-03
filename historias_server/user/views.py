from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from .models import Usuario
from .forms import CreateUsuarioForm, UpdateUsuarioForm
from django.db.models import Q


class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class CreateUsuarioView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    template_name = "user/usuario_create.html"
    model = Usuario
    form_class = CreateUsuarioForm

    def get_success_url(self):
        return reverse("usuarios:lista")

class UpdateUsuarioView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    template_name = "user/usuario_update.html"
    model = Usuario
    form_class = UpdateUsuarioForm

    def get_success_url(self):
        return reverse("usuarios:lista")
    
    def get_object(self, queryset=None):
        obj = get_object_or_404(Usuario, uuid=self.kwargs["uuid"])
        return obj

class DeleteUsuarioView(LoginRequiredMixin, AdminRequiredMixin, DeleteView):
    model = Usuario
    success_url = reverse_lazy("usuarios:lista")

    def get_object(self, queryset=None):
        obj = get_object_or_404(Usuario, uuid=self.kwargs["uuid"])
        return obj


class UsuarioListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = Usuario
    paginate_by = 10

    def get_queryset(self):
        full_name = self.request.GET.get('full_name', "")
        username = self.request.GET.get('username', "")
        email = self.request.GET.get('email', "")
        rol = self.request.GET.get('rol', "")

        query = Usuario.objects.filter(
            (Q(first_name__icontains=full_name) | Q(last_name__icontains=full_name)) &
            Q(username__icontains=username) &
            Q(email__icontains=email)
        )
        if rol != "":
            query = query.filter(rol=rol)
        return query
    
    def get_context_data(self, **kwargs):
        base_url = self.request.GET.copy()
        if "page" in base_url:
            base_url.pop("page")
        context = super(UsuarioListView, self).get_context_data(**kwargs)
        context["full_name"] = self.request.GET.get('full_name', "")
        context["username"] = self.request.GET.get('username', "")
        context["email"] = self.request.GET.get('email', "")
        context["rol"] = self.request.GET.get('rol', "")
        context["base_url"] = base_url.urlencode

        return context
