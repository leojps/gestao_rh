from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from .models import Departamento


class DepartamentosList(ListView):
    model = Departamento


class DepartamentoEdit(UpdateView):
    model = Departamento
    fields = ['nome']
    success_url = reverse_lazy('list_departamentos')


class DepartamentoDelete(DeleteView):
    model = Departamento
    success_url = reverse_lazy('list_departamentos')


class DepartamentoCreate(CreateView):
    model = Departamento
    fields = ['nome']
    success_url = reverse_lazy('list_departamentos')

"""    def form_valid(self, form):
        funcionario = form.save(commit=False)
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=funcionario.nome.split(' ')[0])
        funcionario.save()
        return super(FuncionarioCreate, self).form_valid(form)
"""
