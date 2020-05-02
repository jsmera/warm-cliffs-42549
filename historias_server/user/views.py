from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Usuario
from .forms import UsuarioForm


class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class CreateUsuarioView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    template_name = "user/usuario_create.html"
    model = Usuario
    form_class = UsuarioForm
    success_url = "/"


class UsuarioListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = Usuario
    paginate_by = 10
